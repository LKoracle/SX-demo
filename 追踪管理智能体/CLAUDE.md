# 追踪管理智能体 · 项目说明

## 项目背景

本项目是平安人寿内勤系统**平安DO**上的一个 AI 智能体，面向寿险**营销管理人员**（内勤/机构经理层），帮助其完成从面谈筹备、面谈执行、面谈归档到业绩追踪、风险预警、策略干预的全流程追踪管理工作。

## 产品定位

- **产品名称**：追踪管理智能体
- **宿主平台**：平安DO（平安人寿内勤智能工作台，Web 端、APP端）
- **交互方式**：对话式 AI（Chat-based），用户通过自然语言与智能体交互
- **Agent 框架**：OpenClaw（智能体编排平台，平安内部）
- **工具层**：MCP 工具（原子化工具，供 Agent 调用）

## 核心功能模块（优先级）

| 模块 | 优先级 | 核心能力 |
|------|--------|---------|
| 面谈筹备 | P0 | 圈定待面谈名单、生成代理人画像 |
| 面谈执行 | P0 | 谈目标·盘客户·定行动三步法、数字化面谈采集 |
| 面谈档案 | P0 | 目标制定与双端同步、面谈纪要归档 |
| 过程追踪 | P0 | 实时指标追踪、目标偏差诊断 |
| 预警诊断 | P1 | 触发自动化预警、指标下钻分析 |
| 目标测算 | P2 | 智能测算代理人目标值 |
| 策略干预 | P2 | 匹配干预方案库、生成行动计划 |

## 技术架构（四层）

```
交互层
  └─ 平安DO · 追踪管理智能体（统一对话入口）
          ↓
Agent 应用层（= OpenClaw 实例）
  ├─ 面谈辅助：精准筹备 / 高效执行 / 规范归档
  └─ 业绩追踪：实时监控 / 风险预警 / 根因诊断 / 策略干预
          ↓
原子化工具层（= MCP 工具）
  ├─ 面谈辅助工具：面谈名单 / 代理人画像 / 目标测算 / 数字化面谈 / 目标制定 / 面谈档案
  └─ 业绩追踪工具：指标追踪 / 偏差诊断 / 自动预警 / 根因分析 / 方案匹配 / 行动计划
          ↓
数据层
  └─ 代理人库 / 客户资源库 / 经营指标库 / 面谈档案库 / 干预方案库
```

**辅助系统：**
- **智能体平台**：智能体编排、工作流编排、技能与插件管理、记忆管理
- **事件驱动引擎**：指标异动驱动 / 流程节点驱动 / 数据状态驱动

## 目标用户

- **主要用户**：寿险机构经理、营业部主任等营销管理人员（内勤侧）
- **使用场景**：日常面谈管理、周期性业绩追踪与预警响应

## 两大功能域说明

### 面谈辅助
面向代理人面谈全流程，覆盖「谈前筹备 → 谈中执行 → 谈后归档」三阶段：
- **面谈筹备**：从总公司下发客户名单中精准圈定重点面谈对象，聚合代理人业绩、客户储备、历史面谈档案生成画像
- **面谈执行**：支持「谈目标·盘客户·定行动」三步法核心流程，AI 生成面谈话术辅助，面谈信息数字化采集
- **面谈档案**：目标制定并存储，内勤平安DO与外勤口袋e双端同步，面谈纪要结构化归档并持续优化话术生成

### 业绩追踪
面向机构经营全周期，覆盖「监控 → 预警 → 诊断 → 干预」闭环：
- **过程追踪**：穿透追踪机构、区、部课的业绩/产能/客开/人力数据，自动对比实际 vs 目标，判断经营健康度
- **预警诊断**：通过快乐平安主动提醒内勤，指标下钻定位下滑原因（营业部、产品线、具体指标）
- **策略干预**：智能检索同类场景经营改善方案与最佳实践，转化为可量化、可追踪的待办任务

## 数据层说明

| 数据库 | 内容 |
|--------|------|
| 代理人库 | 代理人档案、历史业绩、画像标签 |
| 客户资源库 | 客户档案、客温、客价、客群标签 |
| 经营指标库 | 业绩指标、产能指标、客开指标、人力指标 |
| 面谈档案库 | 面谈记录、面谈总结、目标值、行动计划 |
| 干预方案库 | 历史案例、改善方案 |

## 关键文件索引

| 文件 | 说明 |
|------|------|
| `产品功能架构图/追踪管理智能体_功能架构图.html/.png` | 完整四层架构图，含各模块功能与技术标注 |

## 中国平安组织层级

```
二级机构
  └─ 三级机构
       └─ 业务发展区
            └─ 网点
                 └─ 营业部 / 展业课
```

**面谈功能用户范围**：使用追踪管理智能体面谈功能的内勤人员涵盖**三级机构、业务发展区、网点**三个层级。原型图中的'待面谈名单'查看全部功能需支持这三个层级的人员分层筛选（一级：网点 tabs；二级：营业部 chips）。

## M值 / P值职级体系

### M值（管理职级）

| M值 | 中文职级名称 | 备注 |
|-----|------------|------|
| M1  | 组经理 | 最基层管理职 |
| M2  | 高级组经理 | |
| M3  | 资深组经理 | |
| M4  | 部经理&课长 | |
| M5  | （未在原型中明确） | |
| M6  | （未在原型中明确） | |
| M7  | （总监及以上） | |
| M8  | （总监及以上） | |
| M9  | （总监及以上） | |
| M10 | （总监及以上） | |
| M11 | （总监及以上） | |
| M12 | （总监及以上） | 团队看板中 M7–M12 合并展示为"总监及以上" |

> 来源：面谈助手 → 团队看板 → 人力分布数据（`sub:'M1'`~`sub:'M7-12'`）

### P值（代理人绩优等级）

| P值范围 | 中文标签 | 备注 |
|---------|---------|------|
| P1–P2   | 过核    | 通过基本考核 |
| P3      | 潜力绩优 | |
| P4–P6   | 绩优    | |
| P7–P9   | 顶尖绩优 | 团队看板展示为"顶尖绩优 P7+" |

> 来源：面谈助手 → 团队看板 → 绩优分布数据（`sub:'P1-2'`~`sub:'P7-9'`）；代理人工号为 **10 位数字**（如 `0112345678`）

---

## 面谈表单枚举值

> 适用：面谈总结表单（renderSumForm）及面谈档案明细（archiveDetail）中的下拉选项

### 绩优跃迁目标（svc / med 面谈）

钻石、银钻、金钻、双金钻、铂金MVP、黑金MVP、双黑金MVP

### 个客目标（med 面谈）

会员、高级会员、个人客户经理

### 定级目标（med 面谈）

P0、P1、P2、P3、P4、P5、P6、P7、P8、P9

---

## 术语表

| 术语 | 含义 |
|------|------|
| 平安DO | 平安人寿内勤智能工作台（桌面 Web 应用） |
| OpenClaw | 平安内部智能体编排平台（本项目 Agent 运行时） |
| MCP 工具 | 原子化工具层，供 Agent 调用的标准化工具 |
| 口袋e | 平安外勤（代理人）端移动应用 |
| 快乐平安 | 平安内部消息推送/通知渠道 |
| 面谈三步法 | 谈目标·盘客户·定行动，面谈执行核心流程 |
| 客温/客价 | 客户温度（活跃度）/ 客户价值，客户资源库中的标签 |
| DO留痕 | 操作记录同步至平安DO系统留存 |
| 双端同步 | 面谈目标/纪要同时同步至内勤平安DO与外勤口袋e |

## 当前进度

- [x] 产品功能架构图 V1.0 完成
- [ ] PRD 文档
- [ ] 原型图设计
- [ ] 智能体详细交互流程设计
- [ ] MCP 工具接口定义
- [ ] 各功能模块原型细化

## 备注

- 本智能体定位为**内勤侧**工具，非代理人端（C 端）工具
- 架构图版本：V1.0 · 2026年3月

---

## APP 端原型 UI 规范（AskBob 对话页）

> 适用文件：`原型图/APP端20260530版本.html`
> 规范版本：v1.0 · 2026年5月

---

### 一、色彩系统

| Token | 值 | 用途 |
|---|---|---|
| Primary | `#1976e8` | 主色：按钮、选中态、链接、发送键 |
| Primary-dim | `rgba(25,118,232,0.08)` | 主色 hover 背景 |
| Primary-shadow | `rgba(25,118,232,0.22)` | 主色阴影（气泡、按钮） |
| Dark-1 | `#1e293b` | 主文本、标题 |
| Dark-2 | `#475569` | 正文、图标（topbar） |
| Dark-3 | `#64748b` | 次级文本、侧边栏图标 |
| Muted | `#94a3b8` | 辅助文本、占位说明 |
| Placeholder | `#cbd5e1` | 输入框 placeholder |
| BG-page | `#f0f2f5` | 聊天页背景 |
| BG-card | `#ffffff` | 卡片背景 |
| BG-muted | `#f8fafc` | 卡片内次级区域 |
| BG-subtle | `#f1f5f9` | icon 背景、分隔区域 |
| Border-default | `#e2e8f0` | 通用边框 |
| Border-strong | `#d1d5db` | 强调边框 |
| Success | `#059669` | 已完成状态 |
| Success-border | `#a7f3d0` | 已完成状态边框 |
| Success-bg | `#f0fdf9` | 已完成状态背景 |
| Error | `#dc2626` | 逾期/危险状态 |
| Error-border | `#fca5a5` | 逾期状态边框 |
| Error-bg | `#fff7f7` | 逾期状态背景 |
| AskBob-icon | `#1a1a2e` | AskBob 品牌图标背景 |
| Sidebar-bar | `#1976e8` | 侧边栏顶部状态栏 |

> **禁止**在 UI 中使用渐变色（包括 border-image/gradient border），统一使用 `Border-default` 或 `Primary` 单色描边。

---

### 二、字体规范

**字体族**：`-apple-system, 'PingFang SC', 'Helvetica Neue', sans-serif`

| 层级 | 大小 | 字重 | 颜色 | 用途 |
|---|---|---|---|---|
| Page Title | 17px | 700 | Dark-1 | Topbar 标题 |
| Section Title | 14px | 700 | Dark-1 | 卡片区块标题 |
| Card Title | 13px | 700 | Dark-1 | 卡片内标题、代理人姓名 |
| Body | 13px | 400 | Dark-1 | 气泡正文、列表内容 |
| Label | 12px | 500 | Dark-2 | 操作标签、chip 文字 |
| Meta | 11px | 400 | Dark-3 | 话题行、辅助说明 |
| Caption | 10px | 400/500 | Muted | 部门路径、状态徽标 |

**行高**：正文段落 `1.65`；单行标签 `1`

> **禁止**对中文内容使用 `font-style: italic`。

---

### 三、图标规范

- **格式**：SVG inline，stroke-based（描边风格）
- **禁止**使用 emoji 作为功能图标
- **描边属性**：统一 `stroke-linecap="round" stroke-linejoin="round"`
- **线宽**（按尺寸）：

| 图标尺寸 | stroke-width |
|---|---|
| 20–22px（topbar） | 2.0–2.4 |
| 16–18px（输入栏） | 1.8 |
| 13–14px（chip、菜单） | 2.0 |
| 12px（展开箭头） | 2.4 |

- **颜色**：topbar 图标用 `Dark-2 (#475569)`；侧边栏/卡片图标用 `Dark-3 (#64748b)`；功能宫格图标外框用 `AskBob-icon (#1a1a2e)` / 细节用 `Primary (#1976e8)`
- **功能宫格图标**：26×26px viewport，`stroke-width 1.8`，外形用 `#1a1a2e`，内部细节用 `#1976e8`

---

### 四、组件规范

#### 4.1 消息气泡

**AI 气泡**（`.chat-ai-bubble`）
- 背景：white；边框：`1px solid #e2e8f0`
- 圆角：`4px 14px 14px 14px`（左上小角）
- 内边距：`12px 14px`；宽度：290px
- 阴影：`0 1px 4px rgba(0,0,0,0.05)`

**用户气泡**（`.chat-user-bubble`）
- 背景：`#1976e8`；文字：white
- 圆角：`14px 4px 14px 14px`（右上小角）
- 内边距：`10px 14px`；最大宽度：240px
- 阴影：`0 2px 8px rgba(25,118,232,0.22)`

> 两种气泡的字号、字重、行高相同（13px / 400 / 1.65），仅位置和配色相反。

#### 4.2 思考卡片（`.think-card`）

与 AI 气泡相同的边框/圆角/阴影，最大宽度 268px。
- 转圈动画：`#1976e8`，done 态转为绿色（`#16a34a` 上边框）
- 标签文字：12px，Dark-3
- 步骤文字：11px，Muted
- 展开箭头：`#94a3b8`，open 时旋转 180°

#### 4.3 面谈对象卡片（`.interview-card`）

- 容器：white，`border: 1px solid #e2e8f0`，圆角 `4px 14px 14px 14px`，宽 290px
- 头部（`.ic-header`）：背景 BG-muted，13px/700，count 徽标用 `#e2e8f0` 背景
- 列表区（`.ic-list`）：背景 `#f4f6fa`
- 条目（`.ic-item`）：圆角 10px，白底，边框 `#e2e8f0`，头像 32×32px 圆形
- 状态徽标（`.ic-status`）：10px/500，`border-radius: 4px`，三态颜色见色彩系统

#### 4.4 快捷回复 Chip（`.entry-chip`）

圆角 20px；边框 `1px solid #dbeafe`；背景 white；字号 12px/500；颜色 Primary；
阴影 `0 1px 3px rgba(25,118,232,0.08)`

#### 4.5 首页快捷操作（`.askbob-shortcut`）

圆角 20px；边框 `1px solid #e2e8f0`；背景 BG-muted；字号 12px；颜色 Dark-1

> `entry-chip`（AI 回复后的跟进建议）用蓝色系，`askbob-shortcut`（主页预设入口）用中性系，两者有意区分。

#### 4.6 输入栏（`.chat-input-bar`）

- 外层 padding：`10px 14px 24px`
- 输入框容器：圆角 24px，边框 `#e2e8f0`，背景 BG-page，阴影 `−3px 0 10px rgba(0,0,0,0.07), 0 −2px 8px rgba(0,0,0,0.05)`
- 图标按钮：34×34px 圆形，opacity 0.55，`:active` 时 opacity 0.85
- 发送按钮：34×34px 圆形，Primary 背景，阴影 `0 2px 6px rgba(25,118,232,0.35)`

#### 4.7 侧边栏（`.chat-sidebar`）

- 宽度 260px，从左侧 slide-in，过渡 `0.28s cubic-bezier(0.22,1,0.36,1)`
- 状态栏背景 Primary（`#1976e8`）
- 历史条目：13px，Dark-2，底部 `0.5px solid #f1f5f9`
- 右键菜单（`.sb-ctx-menu`）：白底，圆角 10px，阴影，**图标必须用 SVG**，不得使用 emoji

---

## PC 端原型 UI 规范（AskBob 对话页 + 工作台）

> 适用文件：`原型图/PC端20260711版本.html`
> 规范版本：v1.0 · 2026年6月

---

### 一、色彩系统

> PC 端主色为 `#2563eb`，区别于 APP 端的 `#1976e8`，两端不互换。

| Token | CSS 变量 | 值 | 用途 |
|---|---|---|---|
| Primary | `--primary` | `#2563eb` | 主色：按钮、选中态、链接、发送键 |
| Primary-light | `--primary-light` | `#3b82f6` | hover 边框、focus ring |
| Primary-dark | `--primary-dark` | `#1e40af` | hover 按钮背景 |
| Primary-pale | `--primary-pale` | `#eff6ff` | 主色浅底（chip hover、badge 背景） |
| BG-deep | `--bg-deep` | `#0f172a` | 顶部导航栏背景 |
| BG-nav | `--bg-nav` | `#1e293b` | 导航辅助背景 |
| BG-sidebar | `--bg-sidebar` | `#f8fafc` | 左侧边栏背景、卡片次级区域 |
| BG-main | `--bg-main` | `#f1f5f9` | 页面主背景 |
| BG-card | `--bg-card` | `#ffffff` | 卡片、输入框背景 |
| Text-primary | `--text-primary` | `#1e293b` | 主文本、标题 |
| Text-secondary | `--text-secondary` | `#64748b` | 正文、次级说明 |
| Text-muted | `--text-muted` | `#94a3b8` | 辅助文本、占位符、图标 |
| Border | `--border` | `#e2e8f0` | 通用边框 |
| Border-light | `--border-light` | `#f1f5f9` | 卡片内部分隔线 |
| Accent-orange | `--accent-orange` | `#f59e0b` | 警告、待办 |
| Accent-green | `--accent-green` | `#10b981` | 成功、新增 |
| Accent-red | `--accent-red` | `#ef4444` | 危险、退出按钮 |
| Shadow-sm | `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | 卡片阴影 |
| Shadow-md | `--shadow-md` | `0 4px 12px rgba(0,0,0,0.08)` | 悬浮阴影 |
| Shadow-lg | `--shadow-lg` | `0 8px 24px rgba(0,0,0,0.12)` | 模态/全屏阴影 |
| Radius | `--radius` | `12px` | 卡片标准圆角 |
| Radius-sm | `--radius-sm` | `8px` | 小圆角（思考卡片、筛选面板） |
| Radius-xs | `--radius-xs` | `6px` | 超小圆角（chip 内部按钮） |

---

### 二、字体规范

**字体族**：`'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif`（区别于 APP 端的 PingFang SC）

**基准字号**：`body { font-size: 14px }`

| 层级 | 大小 | 字重 | 颜色 | 用途 |
|---|---|---|---|---|
| Page Title | 18px | 700 | Text-primary | 欢迎词标题 |
| Nav Logo | 16px | 600 | #fff | 顶部导航 Logo 文字 |
| Sidebar Brand | 18px | 700 | Text-primary | 左侧 "AskBob" 品牌名 |
| Body | 14px | 400 | Text-primary | 导航菜单、侧边栏条目 |
| Card Body | 13.5px | 400 | Text-primary | AI/用户气泡正文，行高 1.7 |
| Label | 13px | 500/600 | Text-secondary | Panel 标题、输入 placeholder |
| Meta | 12px | 400/500 | Text-secondary | 推荐问 chips、辅助文字 |
| Caption | 11–12px | 400/500 | Text-muted | 辅助说明、数据单位 |
| Micro | 10–11px | 400 | Text-muted | 图例标签、徽标 |

> 禁止对中文使用 `font-style: italic`。

---

### 三、整体布局

```
┌─────────────────────────────────────────────────────────┐
│  Top Nav  52px  bg:#0f172a                              │
├────────────┬──────────────────────┬─────────────────────┤
│ Left       │  Center (flex:1)     │  Workbench Panel    │
│ Sidebar    │  bg-main → chat-frame│  (绝对定位，右侧铺满)  │
│ 260px      │  max-width: 400px    │  bg:#eef3f9         │
│ bg-sidebar │  （工作台打开时收窄）  │  left 由 JS 动态写入  │
└────────────┴──────────────────────┴─────────────────────┘
```

- `app-body` 高度 = `calc(100vh - 52px)`，`overflow: hidden`
- 左侧栏可折叠至 52px（icon-only rail），过渡 `width 0.25s ease`
- 工作台打开时：`app-body` 加 `.workbench-open`，中间面板 max-width 收窄至 400px，工作台面板以绝对定位铺满右侧，动画曲线 `1.3s cubic-bezier(0.22,1,0.36,1)`
- 工作台全屏态：`app-body` 加 `.workbench-fullscreen`，工作台面板从 52px 轨道边缘起铺满整屏

---

### 四、顶部导航（Top Nav）

| 元素 | 规格 |
|---|---|
| 高度 | 52px，背景 `#0f172a` |
| 底部装饰线 | `linear-gradient(90deg, transparent, rgba(59,130,246,0.5), transparent)` 高度 1px |
| Logo 图标 | 32×32px，`border-radius:8px`，Primary→#60a5fa 渐变，"DO" 15px/700 白色 |
| 导航链接（激活） | 13px/500，白色；底部 2px `#3b82f6` 下划线，`border-radius:2px 2px 0 0` |
| 导航链接（非激活） | 13px/400，`rgba(255,255,255,0.6)`，hover 0.9 |
| 右侧图标 | 18×18px，`opacity:0.5`，hover `0.9` |
| 头像圈 | 28×28px，Primary→#60a5fa 渐变 |

---

### 五、左侧边栏

| 元素 | 规格 |
|---|---|
| 宽度 | 260px（折叠后 52px，过渡 `0.25s ease`） |
| 背景 | `#f8fafc`，右边框 `1px solid #e2e8f0` |
| 品牌区 | 返回按钮 28×28px + "AskBob" 18px/700 + 折叠按钮 28×28px |
| 新建对话按钮 | dashed border `#e2e8f0`，14px/500，hover `border-color: text-muted` |
| 导航条目 | 14px/400，text-secondary，`padding:9px 10px`，`border-radius:8px` |
| 导航图标 | 18×18px，`opacity:0.6` |
| 历史条目（激活） | white 背景，`border-color:#e2e8f0`，`box-shadow:shadow-sm` |
| 滚动条 | 宽 4px，`background:#d4d4d4`，`border-radius:4px` |
| 退出按钮 | `border:1px solid border`，hover `background:#fef2f2 / border #fca5a5 / color accent-red` |
| 折叠后图标 | 36×36px，居中，无文字标签 |

---

### 六、消息气泡

**AI 气泡**（`.msg-bubble.ai-bubble`）
- 背景 white；边框 `1px solid #e2e8f0`；`border-top-left-radius: 4px`（其余 14px）
- 内边距 `12px 16px`；最大宽度 85%；字号 13.5px，行高 1.7
- 阴影 shadow-sm；入场动画 `msgIn 0.3s ease-out`（translateY 8px + opacity）

**用户气泡**（`.msg-bubble.user-bubble`）
- 背景 `#2563eb`；文字 white；`border-top-right-radius: 4px`（其余 14px）
- 内边距 `12px 16px`；最大宽度 85%

**工具结果气泡**（`.msg-bubble.tool-bubble`）
- 继承 ai-bubble，`max-width: 75%; width: 75%`

---

### 七、思考卡片（`.thinking-card`）

- 背景 BG-sidebar；边框 `1px solid border`；圆角 `--radius-sm`（8px）；`padding:12px 14px`
- Spinner：14×14px，`border-top-color: #2563eb`，done 态 `display:none`
- 文字：12px/500，text-muted
- Body：13px，text-secondary，行高 1.7；折叠 `max-height: 4.8em`
- 展开/收起按钮：primary 色，12px/500，箭头旋转 180°

---

### 八、推荐问滚动区（`.recommend-section`）

- 位于消息区底部、输入栏顶部之间
- 内容水平轮播 `animation: recScrollLR 22s linear infinite`，hover 暂停
- 左右遮罩：`mask-image: linear-gradient(90deg, transparent, #000 4%, #000 96%, transparent)`
- 每条 item：`border-radius:20px`，`bg:#f8fafc`，`border:1px solid #e2e8f0`，13px，text-secondary
- Hover：`bg:#eff6ff`，`border:#bfdbfe`，`color:#2563eb`

---

### 九、选项卡片（Path Options）

**单选**（`.path-option`）
- 容器：`padding:8px 14px`，`border-radius:10px`，`border:1px solid #e2e8f0`
- 指示点：18×18px 圆形，选中 = Primary 填充 + 内部 6×6px 白色圆点
- 选中态：`border-color:#3b82f6`，`background:#eef2ff`，左侧 3px Primary 竖条（`::before`）
- Hover（未选中）：`border-color:#c7d2fe`，`background:#f8faff`，`translateX(2px)`

**多选**（`.path-option-multi`）
- 指示框：18×18px，`border-radius:4px`（方形）
- 选中：Primary 填充 + 白色勾
- 确认按钮：`padding:7px 22px`，Primary bg，`border-radius:8px`，13px/600，置于 `.path-multi-confirm-row` 右对齐

---

### 十、工作台面板（Workbench Panel）

工作台面板是 PC 端特有的右侧工作区，通过 AI 对话触发后从右侧滑入。

#### 10.1 面板结构

```
#workbench-panel（绝对定位，position:absolute）
├── .board-edge-tabs（左边缘竖条按钮组）
│     └── .board-edge-btn（切换工作台的标签页）
└── .board-panel（主面板）
      ├── .board-titlebar（标题栏）
      └── 内容区（各工作台 div，display:none/flex 切换）
```

#### 10.2 标题栏（`.board-titlebar`）

```
背景：white；底边框 1px solid #e2e8f0；padding:14px 24px
左侧：.board-title-icon（32×32px，border-radius:8px，蓝色渐变背景）+ 标题文字（15px/600）+ 版本徽标
右侧：全屏按钮（.board-fullscreen-btn，Primary 蓝色底，白色图标）
```

#### 10.3 左边缘切换按钮（`.board-edge-btn`）

- 初始：18×48px，白色半透明背景，`border-radius:0 8px 8px 0`，`opacity:0.55`
- Hover：宽度扩至 26px，Primary 蓝背景，`opacity:1`
- 全屏按钮（`.board-fullscreen-btn`）：常态即 Primary 蓝色，突出引导点击

#### 10.4 工作台内控制栏

每个工作台（达钻潜力 / 钻石达成 / 承保代理人 / 面谈对象）顶部均有控制栏：

```
<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;">
  <div style="display:flex;align-items:center;gap:8px;">   ← 左侧组
    [筛选营业单位 按钮]  [搜索代理人 输入框]
  </div>
  [导出 按钮]                                              ← 右侧
</div>
```

**筛选营业单位按钮**
- `padding:7px 12px`，`border:1px solid #e2e8f0`，`border-radius:8px`，12.5px/500
- 含三线图标 + 文字标签 + ×清空按钮 + 下箭头
- 点击后展开浮动面板（`position:absolute`，五级组织层级树，260px 宽，360px max-height）

**搜索代理人输入框**
- `border:1px solid #e2e8f0`，`border-radius:8px`，`padding:5px 10px`，白色背景
- 内含放大镜 SVG（12×12px）+ `<input>`（`width:110px`，12px，placeholder "搜索代理人…"）
- `oninput` 实时触发对应工作台的筛选函数

**导出按钮**
- `padding:7px 14px`，`border:1px solid #e2e8f0`，`border-radius:8px`，12.5px/500，`color:#64748b`
- Hover：`borderColor:#3b82f6`，`color:#2563eb`，`background:#eff6ff`
- 点击触发 `showToast`（"正在为您下载代理人名单并推送到邮箱，请稍后去邮箱查看"，3000ms）

#### 10.5 代理人列表表格

```
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,0.05);">
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <thead>
      <tr style="background:#f8fafc;border-bottom:1px solid #e2e8f0;">
        <th style="text-align:left;padding:10px 14px;font-weight:600;color:#64748b;font-size:12px;">姓名</th>
        ...
      </tr>
    </thead>
    <tbody id="[workbenchId]TableBody"></tbody>
  </table>
  <div id="[workbenchId]EmptyTip" style="display:none;padding:32px 16px;text-align:center;font-size:13px;color:#94a3b8;">未找到匹配结果</div>
</div>
```

**表头**：`background:#f8fafc`，`font-size:12px`，`font-weight:600`，`color:#64748b`，`padding:10px 14px`
**数据行**：`padding:11px 14px`，`font-size:12px`；数值列 `text-align:right`；hover 行 `background:#f8fafc`
**空态提示**：`padding:32px 16px`，居中，`font-size:13px`，`color:#94a3b8`

#### 10.6 翻页底栏

位于工作台底部，固定高度，`border-top:1px solid #e2e8f0`，各工作台背景色略有区别：

| 工作台 | 背景渐变 |
|--------|---------|
| 达钻潜力 | `linear-gradient(135deg,#eff6ff 0%,#fff 78%)` |
| 钻石达成 | `linear-gradient(135deg,#f5f3ff 0%,#fff 78%)` |
| 承保代理人 | `linear-gradient(135deg,#f0fdf4 0%,#fff 78%)` |
| 面谈对象 | `linear-gradient(135deg,#fdf4ff 0%,#fff 78%)` |

---

### 十一、钻石等级徽标

PC 端代理人列表中的钻石等级以**纯文字彩色**展示（无背景），颜色规则与 APP 端一致：

| 等级 | 颜色 |
|------|------|
| 钻石 | `#1976e8` |
| 银钻 | `#64748b` |
| 金钻 | `#d97706` |
| 双金钻 | `#b45309` |
| 铂金MVP | `#7c3aed` |
| 黑金MVP / 双黑金MVP | `#1e293b` |
| 未达钻 | `#94a3b8` |

---

### 十二、交互规范

| 行为 | 实现方式 |
|---|---|
| 工作台打开 | `app-body.classList.add('workbench-open')`；侧边栏折叠至 52px；`#workbench-panel` left 由 JS 写入 |
| 工作台全屏 | `app-body.classList.add('workbench-fullscreen')`；工作台 left=52px，铺满 |
| 工作台折叠 | `.wb-fold-tab` 点击切换，工作台 left 还原至 100% |
| 工作台切换 | 左边缘 `.board-edge-btn` 点击，各内容 div `display:flex/none` 切换 |
| 筛选营业单位 | `position:absolute` 浮动面板，点击外部 `document.addEventListener('click')` 关闭 |
| 搜索代理人 | `oninput` 实时过滤，比对 `name/outlet/dept` 字段，`display:none/` 显隐行 |
| 翻页 | JS 维护 `_*Page` 变量，`_*ApplyPagedRows()` 重新写入 tbody |
| 发送消息 | 用户气泡立即渲染 → 思考卡片 → 结果卡渲染 |
| 侧边栏折叠 | `sidebar-left.classList.toggle('collapsed')` |
| 输入框 focus | `border-color:#3b82f6`，`box-shadow:0 0 0 3px rgba(59,130,246,0.12)` |

---

#### 4.8 年度 / 季度 / 月度切换控件（Period Picker 规范）

> **适用范围**：所有需要选择时间周期的面板（钻石达成、业绩追踪、客经工作台、面谈总结等）。新增面板必须沿用此规范，禁止自创样式。

---

##### 触发按钮（Trigger）

所有粒度（年 / 季 / 月）的触发按钮样式统一：

```
display:inline-flex; align-items:center; gap:4px;
padding:5px 10px; border-radius:8px;
border:1.5px solid #d1d5db; background:#fff;
cursor:pointer; font-size:12px; font-weight:500; color:#475569;
box-shadow:0 1px 4px rgba(0,0,0,0.05);
```

- 标签文字（`<span>`）：不加额外样式，继承触发按钮字色
- 箭头图标：11×11px，`stroke:#94a3b8`，`stroke-width:2.5`，`stroke-linecap:round`，`<polyline points="6 9 12 15 18 9"/>`
- 展示格式：**年度** → `2026年`；**季度** → `2026年第2季度`；**月度** → `2026年05月`（月份补零）

---

##### 年度 Picker

触发后弹出固定定位下拉列表（非 drum picker）：

- 容器：`position:fixed`，圆角 10px，阴影 `0 4px 20px rgba(0,0,0,0.14)`，`border:1px solid #e2e8f0`，padding `6px`，`min-width:86px`
- 位置：`top: triggerRect.bottom + 6`，`left: triggerRect.left`
- 每项：`padding:9px 18px`，12px，选中 `font-weight:700 / color:#1976e8 / background:#eff6ff`，圆角 6px
- 年份范围：2024 ~ 2028
- 点击外部关闭：`document.addEventListener('click', _close)`

---

##### 季度 Picker

调用 `window._openDrumPicker`，底部上滑 sheet：

```javascript
window._openDrumPicker({
  title: '季度选择',
  leftItems:  [2024,2025,2026,2027,2028].map(y => ({val:y, label:y+'年'})),
  rightItems: [{val:1,label:'第1季度'},{val:2,label:'第2季度'},
               {val:3,label:'第3季度'},{val:4,label:'第4季度'}],
  leftVal: currentYear, rightVal: currentQuarter,
  onConfirm: function(y, q) { /* 更新触发按钮标签文字 */ }
});
```

---

##### 月度 Picker

调用 `window._openDrumPicker`，底部上滑 sheet：

```javascript
window._openDrumPicker({
  title: '日期选择',
  leftItems:  [2024,2025,2026,2027,2028].map(y => ({val:y, label:y+'年'})),
  rightItems: [1,2,3,4,5,6,7,8,9,10,11,12].map(m => ({val:m, label:m+'月'})),
  leftVal: currentYear, rightVal: currentMonth,
  onConfirm: function(y, m) {
    /* 更新标签，月份补零：(m < 10 ? '0' : '') + m */
  }
});
```

---

##### Drum Picker 底部 Sheet（`_openDrumPicker` 实现规范）

- 遮罩：`rgba(0,0,0,0.45)`，覆盖 `.phone-screen`
- Sheet：白底，`border-radius:16px 16px 0 0`，从底部 `translateY(100%)` 滑入，动画 `0.32s cubic-bezier(0.22,1,0.36,1)`
- Header 行：取消（`color:#94a3b8`）/ 标题（15px/600/Dark-1）/ 确认（`color:#1976e8`，font-weight:500）
- 每列滚筒：可见 5 行，每行高 40px；上下各留 2 行 padding（用空白 div 实现）
- 字号按与选中项的距离：距离 0 → `15px / 600 / #1e293b`；距离 1 → `13px / 400 / #94a3b8`；距离 2+ → `11px / 400 / #c8d0dc`
- 选中行标线：选中区域上下各 `1px solid #e2e8f0`（绝对定位覆盖层，`pointer-events:none`）
- 顶底渐变遮罩：`rgba(255,255,255,0.96) → transparent`（高度 = 2 × 40px = 80px）

---

##### 年 / 季 / 月 模式切换（三段 Tab）

仅在需要支持多粒度切换的面板中使用（如业绩追踪、客经工作台）：

- 容器：`background:#f1f5f9`，圆角 8px，`padding:3px`，`border:1px solid #e2e8f0`
- 激活项：`background:#1976e8; color:#fff; font-weight:600; border-radius:6px; padding:6px 14-20px; font-size:13px`
- 非激活项：`color:#94a3b8; font-size:13px; border-radius:6px; padding:6px 14-20px`

---

### 五、交互规范

| 行为 | 实现方式 |
|---|---|
| 打开聊天 | `overlay.classList.add('visible')` |
| 关闭聊天 | 清空追加消息，滚动归零，`remove('visible')` |
| 侧边栏开关 | `classList.add/remove('open')`，同步 dim 遮罩 `show` |
| 我的空间 | `classList.add/remove('show')`，关闭侧边栏后再打开 |
| 发消息 | 用户气泡立即追加 → 400ms 后显示思考流 → 1800ms 后显示结果卡 |
| 点击 chip | 用户气泡立即追加 → 思考气泡（"正在思考中…"，`color:#94a3b8`，不加 italic） |
| 触摸滑动建议框 | `touchstart/touchend` 检测 dx > 40px 切换建议词 |
| 点击外部关闭 picker | `document.addEventListener('click', _c)` 检测 `!picker.contains(e.target)` |
| 滚动到底按钮 | 离底距离 > 阈值时显示，滚动到底后消失 |
