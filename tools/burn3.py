#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 movie\校对3 读取原片 + 已校对 SRT，烧录双语字幕，输出到 movie\_burned。

样式与 burn.py 一致：
  · 字体：思源黑体 Noto Sans SC（_audio\fonts\）
  · 中文 36 号在上，英文 22 号在下
  · 白字黑边，底部居中，距底 26px
  · 视频 mpeg4/XVID q=4，音频 stream copy（不重编码，零音画偏移）

用法：
  python burn3.py L3_movie          # 单个
  python burn3.py all               # 全部 8 部
"""
import os, subprocess, sys, tempfile, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
MOVIE = os.path.dirname(BASE)
SRCDIR = os.path.join(MOVIE, '校对3')
OUTDIR = os.path.join(MOVIE, '_burned')
FONTSDIR = os.path.join(BASE, 'fonts')

NAMES = ['L1_movie', 'L2_movie', 'L3_movie', 'L4_movie',
         'L5_movie', 'L7_movie', 'L8_movie', 'ending']

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 800
PlayResY: 600
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: CN,Noto Sans SC,36,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2.6,0,2,24,24,26,1
Style: EN,Noto Sans SC,22,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,1.6,0,2,24,24,26,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def srt_ts_to_ass(ts):
    m = re.match(r'(\d+):(\d+):(\d+)[,.](\d+)', ts.strip())
    if not m:
        return None
    h, mi, s, ms = m.groups()
    return '%d:%s:%s.%02d' % (int(h), mi, s, int(ms) // 10)


def srt_to_ass(srt_path, ass_path):
    txt = open(srt_path, encoding='utf-8-sig').read().replace('\r\n', '\n')
    blocks = [b for b in txt.strip().split('\n\n') if b.strip()]
    lines_out = []
    for b in blocks:
        ls = b.strip().split('\n')
        if len(ls) < 3:
            continue
        m = re.match(r'(\S+)\s*-->\s*(\S+)', ls[1])
        if not m:
            continue
        st = srt_ts_to_ass(m.group(1))
        et = srt_ts_to_ass(m.group(2))
        if not st or not et:
            continue
        body = [l.strip() for l in ls[2:] if l.strip()]
        cn = [l for l in body if any('\u4e00' <= c <= '\u9fff' for c in l)]
        en = [l for l in body if l not in cn]
        parts = []
        if cn:
            parts.append(r'{\rCN}' + r'\N'.join(cn))
        if en:
            parts.append(r'{\rEN}' + r'\N'.join(en))
        if not parts:
            continue
        text = r'\N'.join(parts)
        lines_out.append('Dialogue: 0,%s,%s,CN,,0,0,26,,%s' % (st, et, text))
    with open(ass_path, 'w', encoding='utf-8') as f:
        f.write(ASS_HEAD)
        f.write('\n'.join(lines_out) + '\n')
    return len(lines_out)


def esc(p):
    return p.replace('\\', '/').replace(':', '\\:')


def burn_one(name, ffmpeg):
    src = os.path.join(SRCDIR, name + '.avi')
    srt = os.path.join(SRCDIR, name + '.srt')
    if not os.path.exists(src):
        print('  ★ 找不到 %s' % src, flush=True)
        return None
    if not os.path.exists(srt):
        print('  ★ 找不到 %s' % srt, flush=True)
        return None

    tmp_ass = os.path.join(tempfile.gettempdir(), name + '.ass')
    n = srt_to_ass(srt, tmp_ass)
    if n == 0:
        print('  ★ %s 解析出 0 条字幕' % name, flush=True)
        return None

    os.makedirs(OUTDIR, exist_ok=True)
    dst = os.path.join(OUTDIR, name + '.avi')

    vf = "ass='%s'" % esc(tmp_ass)
    if os.path.isdir(FONTSDIR):
        vf += ":fontsdir='%s'" % esc(FONTSDIR)

    # -level 5：800x600@30fps 需要 MPEG-4 Level 5（59400 MB/s 上限，
    # 本片 1900MB/帧×30=57000 MB/s）。不加则默认声明 Level 1（176x144@15fps），
    # 与实际不符，严格的解码器可能据此拒绝。加 -level 5 让码流头声明规范。
    cmd = [ffmpeg, '-y', '-hide_banner', '-loglevel', 'error',
           '-i', src, '-vf', vf,
           '-c:v', 'mpeg4', '-vtag', 'XVID', '-q:v', '4', '-level', '5',
           '-c:a', 'copy', dst]

    print('  烧录 %-10s %2d 条字幕 ...' % (name, n), end='', flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(' ★ 失败')
        print('    %s' % r.stderr.strip()[:400])
        return None
    sz = os.path.getsize(dst) / 1048576
    print(' 完成 %6.1f MB' % sz)
    return {'name': name, 'cues': n, 'size': sz, 'path': dst}


def main():
    ffmpeg = None
    try:
        import imageio_ffmpeg
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass
    if not ffmpeg:
        for p in (r'H:\个人工作区\个人开发\个人开发\ffmpeg_9.0\bin\ffmpeg.exe',):
            if os.path.exists(p):
                ffmpeg = p
                break
    if not ffmpeg:
        print('★ 未找到 ffmpeg')
        sys.exit(1)

    sel = sys.argv[1:] or ['all']
    if sel == ['all']:
        sel = NAMES

    print('源目录：%s' % SRCDIR)
    print('输出：  %s' % OUTDIR)
    print('字体：  %s' % ('有' if os.path.isdir(FONTSDIR) else '缺'))
    print('ffmpeg: %s' % ffmpeg)
    print()

    done = []
    for n in sel:
        r = burn_one(n, ffmpeg)
        if r:
            done.append(r)

    print()
    print('完成 %d/%d' % (len(done), len(sel)))
    if done:
        json.dump(done, open(os.path.join(BASE, '_burn_result.json'), 'w'),
                  ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
