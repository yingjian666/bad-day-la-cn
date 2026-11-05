# Bad Day L.A. 简体中文汉化 (Bad Day LA / BadDayLA)

![版本](https://img.shields.io/badge/version-1.1-blue.svg)

![下载量](https://img.shields.io/github/downloads/yingjian666/bad-day-la-cn/total.svg)

![游戏](https://img.shields.io/badge/game-Bad%20Day%20L.A.-orange.svg)

![平台](https://img.shields.io/badge/platform-Windows%20XP%2B-lightgrey.svg)

![许可](https://img.shields.io/badge/license-see%20LICENSE-green.svg)

> **中文名称**：坏日洛杉矶 / 洛杉矶大灾难 / 洛城受难日 / 洛城大灾难  
> **英文名称**：Bad Day L.A. / Bad Day LA / BadDayLA / BadDay L.A.  
> **完整标题**：American McGee's Bad Day L.A.  
> **开发**：Enlight Software　**发行**：Aspyr Media（2006）


> 这游戏的中英文叫法都不统一，上面列的几种写法指的是同一个游戏。
> 本页提供的是一份完整的**汉化补丁 / 中文补丁 / 汉化包**，覆盖界面文本、
> 对话字幕与过场动画，适用于正版 PC 英文版。
> 你不确定找对了没有，可以对照下面的截图和发行信息。

2006 年第三人称动作游戏。主角安东尼（Anthony）是个愤世嫉俗的越战老兵，在洛杉矶当消防员。某个夜里全城同时遭遇地震、火灾、生化袭击、帮派火并和陨石，政府救援彻底瘫痪，他一边骂街一边穿过十个关卡的洛杉矶街景去救人。黑色幽默和辛辣讽刺贯穿全程——对美国消费文化、电视媒体、官僚体系的调侃一刻不停。

原版只有英文，本补丁把它完整汉化。

这是 2006 年的老游戏，国内流传的多是删减过的 RIP 版，界面与文本都与完整版有出入。  
本补丁基于完整的 PC 英文版制作，覆盖全部界面、对话与过场动画，  
可以理解为一份完整的中文补丁。

**本补丁支持正版游戏，反对盗版，不收取任何费用。**

- 基于 **PC 英文版 1.1.0** 制作（Aspyr Media 发行，2006 年，开发商 Enlight Software）
- 原版没有任何中文支持：它是单字节编码引擎，连字符集声明文件 `CODEPAGE.RES` 都是空的
- 补丁不含游戏本体，不含任何未经修改的原始美术、模型、音频、影片、地图资源

---

## 目录

- [效果截图](#效果截图)
- [汉化范围](#汉化范围)
- [技术说明](#技术说明中文是怎么进到-2006-年的引擎里的)
- [安装](#安装)
- [下载](#下载)
- [兼容性](#兼容性)
- [已知问题](#已知问题)
- [仓库结构](#仓库结构)
- [English](#english)　← 英文说明
- [授权](#授权)
- [免责声明](#免责声明)

---

## 效果截图

游戏内过场动画的中文字幕效果（中文在上，英文在下）：

|    |        |
| -- | ------ |
| L1 | L2     |
| L3 | L4     |
| L5 | L7     |
| L8 | ending |

> 截图来自 `BadDayLA_CN_v1.1_with_movies.zip` 那个包的成品，该包包含过场动画的中文字幕版，见 [下载](#下载)。

---

## 汉化范围

### 已汉化

| 载体                                      | 内容                        | 数量              |
| --------------------------------------- | ------------------------- | --------------- |
| `Resource\t_interf.txr`                 | 界面文本：主菜单、选项、存档界面、HUD、任务提示 | 153 条           |
| `Resource\t_basic.txr`                  | 日期、时长、数字等格式串              | 40 条            |
| `scenario\scenario.res` / `.rex`        | 关卡名、地点名、时间                | 12 关 × 4 字段     |
| `script\scenario\*.dlg` / `*.dlx`       | 全部对话与过场字幕（含德语副本）          | 44 个文件 / 3004 条 |
| `item\item.res`                         | 物品名称（拾取时弹出的名字）            | 184 条中 120 条    |
| `Resource\credits.txc` / `creditsX.txc` | 制作人员名单                    | 286 / 221 行     |
| `font\*.fin` + `int8x6\*.dds`           | 中文字库（思源黑体字形，自带描边）         | 3 套实际使用         |

### 有意未汉化

| 项                            | 原因                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------- |
| 街道招牌、广告牌、海报等场景贴图             | 德语、西班牙语、英语招牌是洛杉矶街景的氛围组成部分，汉化会破坏原作的视觉设计                                           |
| 品牌名与武器型号：`Julky`、`UZI`、`RPG` | 字节预算不足（`UZI` 只占 3 字节，而「乌兹」要 4 字节，数据块零余量，无法腾挪）；`Julky` 是游戏内饮料品牌，有独立罐身贴图，译成中文反而对不上 |
| 程序异常时的系统错误弹窗                 | 属于异常路径，正常游戏不会出现                                                                  |

### 补丁改了什么、没改什么

改动的只有 **63 个文件**：

| 类别   | 数量 | 文件                                                                        |
| ---- | -- | ------------------------------------------------------------------------- |
| 主程序  | 1  | `BadDayLA.exe`                                                            |
| 文本表  | 5  | `t_interf.txr`、`t_interfX.txr`、`t_basic.txr`、`credits.txc`、`creditsX.txc` |
| 编码声明 | 1  | `codepage.res`（原版是空文件）                                                    |
| 关卡配置 | 2  | `scenario.res`、`scenario.rex`                                             |
| 物品定义 | 1  | `item.res`                                                                |
| 单位定义 | 1  | `unit.res`                                                                |
| 对话字幕 | 44 | `script\scenario\*.dlg` / `*.dlx`（含德语副本）                                  |
| 中文字库 | 6  | 3 套 `.fin` + 3 套 `.dds`                                                   |
| 菜单位图 | 2  | `gamemenu.dds`、`maingame.dds`                                             |

**没有改动**：全部模型、场景贴图、音频、影片、地图、动画，以及 `DFEngine.dll`、`OpenAL32.dll` 等引擎组件——与原版逐字节相同。

`texture\` 和 `textureL\` 下所有招牌、广告、海报一个像素都没动。

---

## 技术说明：中文是怎么进到 2006 年的引擎里的

这部分是本项目的核心工作量。原版引擎有完整的多语言框架，但没有实现任何双字节支持，而且文本绘制链路上有多处硬编码假设，每一处都会单独把中文打死。

### 概览

| # | 障碍       | 表现                        | 处理方式                        |
| - | -------- | ------------------------- | --------------------------- |
| 1 | 编码模式进不去  | 中文全部空白                    | 改编码模式跳转表                    |
| 2 | 取字符、前进函数 | ASCII 被两两合并成乱码，换行失效       | 在新增节写机器码替换                  |
| 3 | 字符数统计    | 血量 `100` 显示成 `10`，右对齐文字被切 | 同上（第四个 vtable）              |
| 4 | 字库格式     | 无从生成中文字形                  | 逆向 `.fin` / `.dds` 格式，自写生成器 |
| 5 | 字形拉伸     | 全角冒号被拉成 `〓` 方块            | 修正字形记录的前进距离字段               |

### 1. 编码模式：写了配置也不生效

引擎按 `CODEPAGE.RES` 选择编码模式，但**无论你怎么写，它只会进模式 1**。模式 1 的取字符函数调用 CRT 的 `_mbslen` 一族，依赖 CRT locale——而游戏从未调用 `setlocale()`，locale 永远是默认的 `"C"`，中文被当成非法序列，一个都画不出来。

实测读运行时内存 `0x7633C8`，始终得到 `0x0053CF60`（模式 1），从不变成 `0x0053CF70`（GBK 双字节）。

解法是在脚本函数 `FUN_0053C9D0` 的模式跳转表上动手。表在 `0x53CED8`（文件偏移 `0x13CED8`），四项分别指向四种编码实现。把**索引 1 的指针从模式 1 改成模式 2**：

```
文件偏移 0x13CEDC:  0x0053CB3C  →  0x0053CC40
```

这样不管配置文件怎么写、走哪个分支，最终都会装成 GBK 双字节 vtable。改完主菜单五项中文完整显示。

### 2. 取字符与前进：模式 2 是无条件双字节

模式 2 的实现假设所有字符都是双字节：

```asm
mov ch,[eax] ; mov cl,[eax+1]     ; 无条件读两个字节
add [ecx],2                        ; 无条件前进两字节
```

后果是 ASCII 被两两合并（`Ve` → `0x5665` → 显示成「腕」），`\r\n` 被当成一个汉字（换行失效，七条菜单挤成一行）。

于是在 exe 新增的 `.asciix` 节里手写两个函数，按首字节判断宽度：`< 0x81` 走单字节，`>= 0x81` 走双字节（GBK 双字节首字节范围是 `0x81`–`0xFE`）。再改模式 2 的 vtable 设置指令，把函数指针指过去：

```
0x53CC4B  mov [0x7633C8], 0x53CF70   →  0x7DE300   (取字符)
0x53CC55  mov [0x7633CC], 0x53D020   →  0x7DE31B   (前进)
```

### 3. 字符数统计：血量 `100` 变 `10` 的原因

编码系统不是两个函数指针，而是**一整组 vtable**。模式 2 会设置六项，其中第四项「字符数」当初被漏掉了，还是原始实现：

```asm
0053d2d0  mov  eax,[ecx]
0053d2d2  push eax
0053d2d3  call 0x6F0D29      ; CRT 的 _mbslen
```

`_mbslen` 同样依赖 CRT locale，在 `"C"` 下把 GBK 双字节算成**两个字符**。这个值用于文本宽度测量，测出的宽度虚高一倍，右对齐的文字起点就算错。

血量走的是右对齐绘制：

```asm
call FUN_00552ee0     ; 测量宽度
sub  edx, edi         ; X 起点 = 右边界 - 宽度 + 1
```

宽度被算成两倍后，起点跑到屏幕外，末位数字被裁掉——血量 `100` 于是显示成 `10`。

解法同样是手写一个字符数函数（按首字节 `0x81` 判断宽度），挂到第四个 vtable：

```
0x53CC69  mov [0x7633D4], 0x53D2D0  →  0x7DE330
```

顺带把这个问题一起修掉的还有弹药数、计时器、菜单右侧的所有右对齐数字。

### 4. 字库：逆向格式后自己生成

原版字库是一对文件：`font\*.fin`（索引，309590 字节）加 `int8x6\*.dds`（字形图集，2048×2048，16 位 `A4R4G4B4` 未压缩位图）。

`.fin` 是 22110 个槽位的索引表，字符范围 `0xA1A1`–`0xF7FE`（GBK 全集），每槽记录字形在图集里的矩形和度量。逆向清楚后写了生成器 `makefont.py`，把**思源黑体**（Noto Sans SC）烘成 GBK 全集：

```
--ttf "Noto Sans SC" --size 18 --mode gbk --set gb2312 --grid --lineheight 26
--metrics 32,37,9,223,0,4 --atlas 2048x2048
```

字号按原字库的汉字步进反推：原字库汉字步进 18px，所以取 18px，保证一行能放的字数、换行位置、右对齐位置全部不变。**选思源黑体是因为它用 SIL Open Font License 1.1 授权，允许嵌入、修改、再分发**——用系统自带的商业字体（微软雅黑、宋体）烘成位图分发，在字体授权上是有争议的。

两处关键：**度量必须逐字节对齐原版**（`32,37,9,223,0,4`），**字形记录里的前进距离必须填真实值而不是墨迹宽度**。

**描边不是引擎画的，是烘进贴图里的**：字芯纯白 `#FFFFFF`，描边深灰 `#444444`~`#555555`（不是纯黑），中间带抗锯齿。生成的中文字库必须照这个画，否则质感和原版明显不同。

**ASCII 的处理**：字库只含 GBK 区，但界面里有大量英文（版本号、按键名、型号）。解法是把 ASCII 32–126 塞进 GBK 用户区的未使用槽位 `0xAAA1`–`0xAAFF`——注意这会覆盖该区的生僻字（`獲獳獴獵` 之类），游戏不会用到；好处是 `first`/`last` 不变，不会触发引擎的 `Insufficient Memory`。再填一张 ASCII→槽位的映射表（第 i 项值 = `0x900 + i`），由 `.asciix` 里的 hook 查表。

这里踩过一个坑，值得单独说。hook 的查表指令是：

```asm
007de023  0fb78400 00e17d00   movzx eax, word ptr [eax + eax*1 + 0x7DE100]
```

SIB 字节 `0x00` 表示 scale=1，所以地址是 `0x7DE100 + 2 × index`，**步长 2 字节**。一开始按常见的 `[eax+eax*2]` 理解成 3 字节，结果每项都读到相邻项错位的半字节，主菜单右上角的版本号变成了 `DN霾霾霾霾霾`。改回 2 字节后 `Ver.1.1.0` 正常显示。

各套字库的 `first` 必须统一为 `0xA1A1`，否则 hook 里的 `cmp` 判断会跳过映射，ASCII 又变乱码。

### 5. 全角冒号变成 `〓`

标点显示成方块，原因是绘制时屏幕宽度取「前进距离」、贴图 UV 取「墨迹宽度」，两者不一致就会被拉伸：

| 字符  | 墨迹宽  | 前进距离 | 拉伸比     |
| --- | ---- | ---- | ------- |
| `：` | 2px  | 18px | **9.0** |
| `。` | 3px  | 18px | 6.0     |
| 汉字  | 15px | 18px | 1.2     |

两个点的冒号被横向拉伸 9 倍，就成了两道横杠。汉字拉伸比只有 1.2，肉眼看不出来，所以只有标点出问题。

修法是生成器里把记录中的 `x2` 按前进距离算（`x2 = u + adv - 1`），而不是按墨迹宽度算。全部字库重新生成后消失。

### 6. 文本载体格式

三类载体，约束各不相同：

| 格式              | 结构                                           | 改文本的约束                      |
| --------------- | -------------------------------------------- | --------------------------- |
| `.txr` / `.txc` | 条目数 + 分类表 + `序号\|分类\|序号\|文本`                 | **变长安全**，可自由改长度             |
| `item.res`      | 4 字节条目数 + 184 条 × 38 字节索引（32 名字 + 4 偏移）+ 数据块 | **必须等长**，块内零余量，译文不能超过原字节数   |
| `scenario.res`  | 4 字节条目数 + 12 条 × 38 字节索引 + 定长文本块             | **必须等长**，差额从尾随空格借还          |
| `.dlg` / `.dlx` | `[关卡ID][条目ID]` + 台词 + `~` 分隔                 | 按 ID 关键字索引，可自由变长，但不能增删 ID 行 |

### 完整改动清单

主程序共 **6 处改动**：4 处是指针/立即数改写，2 处是往末尾的可执行节 `.asciix` 里写数据（该节原本只用来放一个 ASCII hook，后面大片空闲）。

| # | 位置（文件偏移）            | 原值           | 改后                  | 作用             |
| - | ------------------- | ------------ | ------------------- | -------------- |
| 1 | `0x13CEDC`          | `0x0053CB3C` | `0x0053CC40`        | 编码模式强制 GBK     |
| 2 | `0x13CC51`          | `0x0053CF70` | `0x007DE300`        | 取字符 → 智能判断     |
| 3 | `0x13CC5B`          | `0x0053D020` | `0x007DE31B`        | 前进 → 智能判断      |
| 4 | `0x13CC6F`          | `0x0053D2D0` | `0x007DE330`        | 字符数 → 智能判断     |
| 5 | `0x396100` 起 190 字节 | 错位映射表        | 95 项，每项 `0x900 + i` | ASCII → GBK 槽位 |
| 6 | `0x396300` 起        | 空白           | 三个函数的机器码            | 智能宽度判断         |

手写机器码时，跳转的相对偏移必须逐字节算准。第一次写取字符函数时 `jb` 的 rel8 少算了 1 字节（写了 `0x09`，应为 `0x0C`），跳到了 `ret` 上，把**指针地址**当字符码返回，游戏直接白屏卡死。之后每次写完都用 capstone 反汇编回读，逐个核对跳转目标是否落在预期标号上。

没有新增任何 API 依赖：导入表与原版逐一对齐（16 个 DLL、274 个函数，零新增）。PE 头子系统版本仍是 4.0，字体零系统依赖（字库是预烘焙位图，不调用 `CreateFont`，目标机器装不装中文字体都不影响），因此在 Windows XP 上同样可运行，唯一前提是原版就要求的 DirectX 9.0c。

详细的逆向过程、失败实验和排错记录见 [TECHNICAL.md](TECHNICAL.md)。

---

## 安装

1. **备份**游戏目录。至少备份 `BadDayLA.exe`、`Resource\`、`script\`。
2. 把补丁包内所有文件夹解压覆盖到**游戏根目录**（`BadDayLA.exe` 所在的那一层）。
3. 运行 `BadDayLA.exe`，无需任何额外设置。

补丁不含 `CONFIG.DAT` 和 `SAVE\`，不会覆盖你的画面设置与存档。

**字库与文本只在启动时加载一次**：如果游戏正在运行，请先完全退出进程，覆盖后再启动才生效（只退回主菜单不算）。

文字显示异常时依次检查：是否覆盖到了正确目录、是否完全退出后重启、系统是否为简体中文环境（补丁使用 GBK 编码）。


卸载方式：用备份的目录覆盖回来即可。本补丁不写注册表，不写系统目录，不联网。

## 下载

[**↓ 下载 v1.1**](../../releases/latest)

| 文件 | 大小 | 说明 |
|---|---|---|
| `BadDayLA_CN_v1.1.zip` | 4.1 MB | **推荐**。纯文本汉化，覆盖到游戏目录即可 |
| `BadDayLA_CN_v1.1_with_movies.zip` | 484 MB | 额外含 8 个过场动画的中英双语字幕版 |
| `SHA256SUMS.txt` | — | SHA256 校验和 |

两个包的游戏内文本效果完全一致，区别只在过场动画：

- **纯文本包**（4.1 MB）：过场动画保持英文原版画面，只汉化界面与对话字幕
- **含动画包**（484 MB）：把 480 MB 的过场动画重新编码并烧入中文字幕

含动画包体积大，是因为 8 个 avi 都是游戏原片重制的修改版本，属游戏资源衍生内容，
详见包内 `movie\影片字幕说明.txt` 的版权声明。只想要中文界面的话，下载 4.1 MB 的那个就够。

## 兼容性

| 系统 | 状态 | 说明 |
|---|---|---|
| Windows XP SP2 / SP3 | ✅ 已验证格式 | 游戏引擎内嵌 FFmpeg，不依赖系统解码包 |
| Windows 7 / 8 / 10 / 11 | ✅ 已验证 | |
| 简体中文环境 | ✅ 必须 | 补丁使用 GBK 编码，非中文系统需装语言包 |

### Windows XP 说明

游戏引擎文件 `DFEngine.dll` 内嵌了 FFmpeg/libavcodec 的 MPEG-4 解码模块，
不依赖系统安装 Xvid 或 DivX 解码包。补丁本身不含任何影片文件，只替换文本、
字库与主程序，与原版资源格式完全一致，XP 上不存在额外兼容性问题。

补丁不写注册表，不写系统目录，不联网，不安装任何服务或驱动。

---

## 仓库结构

```
bad-day-la-cn/
├── README.md                          本文件
├── TECHNICAL.md                       技术实现细节（逆向分析、地址、字节）
├── CHANGELOG.md                       版本记录
├── LICENSE                            授权条款
├── subtitle/                          字幕源文件（SRT，可提 PR 校对）
│   ├── L1_movie.srt
│   └── ...
├── tools/
│   └── burn3.py                       字幕烧录脚本（SRT → ASS → 视频）
├── docs/
│   ├── 影片字幕技术档案.txt            影片字幕的完整技术说明（存档）
│   └── screenshots/                   效果截图
└── release-notes/
    └── v1.1.md                        本版发布说明
```

**补丁本体不放在仓库里**（含字库 DDS 共 55 MB，超过 Git 单文件建议值），
请到 [Releases](../../releases) 页面下载。

### 为什么公开技术细节

汉化不是"把文本换成中文"这么简单。这个引擎是 2006 年的单字节设计，
要让它显示中文，需要改编码子系统、逆向字库格式、重新生成带描边的字库贴图，
还要处理四种不同约束的文本容器格式。

`TECHNICAL.md` 记录了完整过程，包括替换函数的具体地址与字节数、
失败方案的原因分析、以及尚未解决的问题。如果以后有人想做同一引擎
其他游戏的汉化，这些内容可以直接复用。

---

## 已知问题

| 问题          | 影响   | 说明                                                                                                     |
| ----------- | ---- | ------------------------------------------------------------------------------------------------------ |
| 加载界面底部文字不显示 | 轻微   | 白色加载画面底部那一行（原本显示「读取中」）中文不显示，画面呈纯白底，约 2 秒。该文字走的是与游戏内不同的绘制路径，累计 7 种方案均未成功，根因已定位到 `0x556065` 调用点的字符串参数不稳定 |
| 超长句子被截断     | 轻微   | 引擎有右边界参数，超过一行宽度即截断（18px 字库约 26 个全角字）。**英文原版同样截断**，属引擎固有行为，不是汉化缺陷                                       |
| 招牌、品牌名保持原文  | 设计如此 | 见上文「有意未汉化」                                                                                             |

## English

**Bad Day L.A. — Simplified Chinese Localization Patch**

A complete Chinese translation patch for *Bad Day L.A.* (also written *Bad Day LA*,
*BadDayLA*; full title *American McGee's Bad Day L.A.*), the 2006 third-person
action game developed by Enlight Software and published by Aspyr Media.

This patch translates **all UI text, dialogue subtitles, item names, level names
and credits** into Simplified Chinese. It works on the retail English PC version
1.1.0.

### Download

See [Releases](../../releases/latest):

| File | Size | Contents |
|---|---|---|
| `BadDayLA_CN_v1.1.zip` | 4.1 MB | Text localization only (recommended) |
| `BadDayLA_CN_v1.1_with_movies.zip` | 484 MB | Also includes 8 cutscene videos with burned-in bilingual subtitles |

Extract over your game folder (where `BadDayLA.exe` lives). Back up first.

### Technical notes

The original engine is a 2006 single-byte design with no CJK support — even the
codepage declaration file `CODEPAGE.RES` ships empty. Making it display Chinese
required patching the encoding subsystem, reverse-engineering the bitmap font
format, and regenerating font atlases with baked-in outlines.

[TECHNICAL.md](TECHNICAL.md) documents the full process: jump table patching,
the three string-handling functions that were replaced (with addresses and byte
counts), the exact cause of the "100 renders as 10" bug, and the four text
container formats with their differing length constraints.

Written in Chinese, but the code blocks, addresses and structure should be
readable regardless.

### Compatibility

Windows XP SP2 and later. The patch writes nothing to the registry, no services,
no network access. Chinese (GBK) system locale required.

### License

Translation text and tooling: CC BY-NC-SA 4.0. Font: SIL OFL 1.1.
Game assets remain the property of their respective owners. See [LICENSE](LICENSE).

---

## 授权

本项目使用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) 协议授权。

- **署名**：转载或二次创作请标明来源
- **非商业性使用**：不得用于商业目的，不得出售、出租、捆绑销售
- **相同方式共享**：基于本项目的二次创作须以相同协议授权

## 免责声明

1. 本汉化补丁为**非官方民间作品**，由爱好者无偿制作、免费发布，与游戏的开发商 Enlight Software、发行商 Aspyr Media 及其关联公司没有任何关系。
2. 本补丁**仅供学习交流与个人研究使用**，请勿用于任何商业用途。
3. **本补丁支持正版游戏，反对盗版。**
   本补丁不包含、不提供游戏本体，也不提供任何未经修改的游戏原始资源文件。

   本补丁所含内容明细：

   - 汉化所需的文本、字库与少量程序修改。

   不含任何原始美术、模型、音频、影片、地图资源。
   使用前请自行获取游戏的合法授权副本。
4. 游戏及其全部素材的著作权归原权利人所有。若权利人认为本项目不当，请联系删除。
5. 本补丁按「现状」提供，不对任何直接或间接损失承担责任。
6. 请在下载后 24 小时内删除，或转为购买正版游戏。
