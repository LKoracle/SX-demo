# 平安DO PC · 追踪管理智能体
## 功能结构说明（基于 PC端20260725版本）

---

## 一、整体页面结构

```
┌─────────────────────────────────────────────────────────┐
│  Top Nav  52px  bg:#0f172a                              │
├────────────┬──────────────────────┬─────────────────────┤
│ Left       │  Center (flex:1)     │  Workbench Panel    │
│ Sidebar    │  bg-main → chat-frame│  （绝对定位，右侧铺满） │
│ 260px      │  max-width: 400px    │  bg:#eef3f9         │
│ bg-sidebar │  （工作台打开时收窄）  │  left 由 JS 动态写入  │
└────────────┴──────────────────────┴─────────────────────┘
```

- `app-body` 高度 = `calc(100vh - 52px)`，`overflow: hidden`
- 左侧栏可折叠至 52px（icon-only rail），工作台打开后自动折叠
- 工作台打开时：中间面板 max-width 收窄至 400px，工作台面板以绝对定位铺满右侧

---

## 二、功能路由总览（routeQuery）

| 触发关键词 | 路由结果 |
|-----------|---------|
| 含"达钻潜力人员" / "达钻潜力" | 展示达钻潜力人员名单工件卡 + 打开达钻潜力工作台 |
| 含"钻石达成" | 展示钻石达成名单工件卡 + 打开钻石达成工作台 |
| 含"面谈对象" | 展示面谈对象工件卡 + 打开面谈对象工作台 |
| 含"保单" | 展示承保代理人工件卡 + 打开承保代理人工作台 |
| 含"开展面谈" | 触发两步式面谈引导流程 |

---

## 三、面谈引导流程（"我要开展面谈"）

用户输入含"开展面谈"关键词后，触发两步追问卡。

### 3.1 Step 1：选择面谈月份

- 选项动态生成：本月 / 下月 / 下下月（显示为"YYYY年MM月"）
- 选项卡片 CSS 类：`.intr-month-opt`
- 用户点击后：
  1. 所有选项锁定（pointer-events none），选中项添加 selected 样式
  2. 整张卡片置灰（opacity 0.6）
  3. 追加用户气泡："面谈月份：YYYY年MM月"
  4. 400ms 后展示 Step 2

### 3.2 Step 2：选择面谈主题

卡片步骤标签"2/2"，含以下选项：

| 类型 | 主题 | 右侧徽标 |
|------|------|---------|
| 固定主题 | 6-8月服务季面谈 | `固定主题` 灰色标签 + 人数 |
| 固定主题 | 医疗险绩优面谈 | `固定主题` 灰色标签 + 人数 |
| 固定主题 | MBO面谈 | `固定主题` 灰色标签 + 人数 |
| AI推荐 | 达钻潜力人员 | `AI推荐` 蓝色标签（无右侧描述文字） |

- 选项卡片 CSS 类：`.intr-theme-opt`
- 用户点击后：
  1. 所有选项锁定（opacity 0.4），选中项保持 opacity 1
  2. 追加用户气泡："面谈主题：XXX"
  3. 400ms 后进入 AI 思考态

### 3.3 AI 思考 + 工件卡渲染

思考行显示"正在筛选面谈对象…"，1400ms 后替换为：
- AI 文案（按主题类型区分）
- 工件卡（可点击，打开对应工作台）

**路由规则（按主题）：**

| 主题 | AI 文案 | 图标 | 点击打开 |
|------|---------|------|---------|
| 达钻潜力人员 | "已为您匹配 YYYY年MM月 距达钻 FYC 差额 300 元内的潜力人员，共 32 人…" | 蓝色星形图标（#2563eb） | 达钻潜力人员名单工作台 |
| 其他三个主题 | "已根据面谈主题为您匹配 YYYY年MM月「XXX」待面谈名单，共 32 人…" | 紫色人群图标（#9333ea） | 面谈对象工作台 |

**工件卡标题格式：**
- 达钻潜力人员：`YYYY年MM月达钻潜力人员名单`
- 其他主题：`YYYY年MM月XXX名单`

---

## 四、工作台面板（Workbench Panel）

### 4.1 面板公共结构

```
#workbench-panel（绝对定位）
├── .board-edge-tabs（左边缘竖条切换按钮）
└── .board-panel（主面板）
      ├── .board-titlebar（标题栏）
      └── 内容区（各工作台 div，display:flex/none 切换）
```

每个工作台顶部均有控制栏：筛选营业单位按钮 + 搜索代理人输入框（左）+ 导出按钮（右）。

### 4.2 操作列（固定右侧）

四个工作台的数据表格均有固定右侧的"操作"列，横向滚动时不随内容移动。

**实现规范：**
- 表格外层：`overflow:hidden`（用于 border-radius）
- 表格滚动容器：`overflow-x:auto`
- `<th>` 操作列：`position:sticky; right:0; z-index:2; box-shadow:-2px 0 6px rgba(0,0,0,0.06)`
- `<td>` 操作列：`position:sticky; right:0; z-index:1; background:#fff; box-shadow:-2px 0 6px rgba(0,0,0,0.06)`；class 为 `op-cell`
- 行悬停同步：TR 的 `onmouseenter/onmouseleave` 同时更新 `.op-cell` 背景色

**查看明细按钮样式：**
```css
border:none; background:transparent; color:#2563eb;
font-size:12px; font-weight:500; cursor:pointer; padding:0;
```
Hover 时 `text-decoration:underline`，无按钮边框/背景。

---

## 五、各工作台详情

### 5.1 达钻潜力人员名单

**触发方式：** 直接 query "达钻潜力" 关键词，或面谈引导流程选择"达钻潜力人员"主题后点击工件卡。

**表格列（min-width 780px）：**

| 列名 | 说明 |
|------|------|
| 姓名 | 代理人姓名 |
| 网点 | 所属网点 |
| 所属营业部/组 | 所属部门 |
| P值 | 绩优等级 |
| M值 | 管理职级 |
| FYC差额 | 距钻石差额，格式"¥XXX 元"，颜色 `#ef4444` |
| 件数差额 | 距钻石件数差，格式"X 件" |
| 操作 | 固定右侧，查看明细按钮 |

**数据源：** `diamondAgentsData`（32条），字段：name / outlet / dept / pVal / mVal / level / gap / gapPieces。

---

### 5.2 钻石达成名单

**触发方式：** query 含"钻石达成"。

**表格列：** 姓名 / 网点 / 所属营业部组 / P值 / M值 / 钻石等级 / 连钻月数 / 操作（固定右侧）。

---

### 5.3 承保代理人名单

**触发方式：** query 含"保单"。

**表格列（min-width 700px）：**

| 列名 | 说明 |
|------|------|
| 姓名 | 代理人姓名 |
| 网点 | 所属网点 |
| 所属营业部/组 | 所属部门 |
| P值 | 绩优等级 |
| M值 | 管理职级 |
| 承保FYP | 格式"¥XX,XXX" |
| 承保件数 | 格式"XX件" |
| 操作 | 固定右侧，查看明细按钮 |

---

### 5.4 面谈对象列表

**触发方式：** query 含"面谈对象"，或面谈引导流程选择固定主题后点击工件卡。

**表格列（min-width 700px）：**

| 列名 | 对齐 | 说明 |
|------|------|------|
| 姓名 | 左 | 代理人姓名 |
| 网点 | 左 | 所属网点 |
| 所属营业部/组 | 左 | 所属部门 |
| P值 | 左 | 绩优等级 |
| M值 | 左 | 管理职级 |
| 面谈主题 | 左 | 多主题时每行一条，与待面谈数量一致 |
| 待面谈数量 | 右 | 纯数字，颜色 `#64748b`（不使用红色等特殊色） |
| 共需面谈数量 | 右 | 纯数字，颜色 `#64748b` |
| 操作 | 中 | 固定右侧，查看明细按钮 |

**数据生成规则（Mock）：**
- 使用 `diamondAgentsData.slice(0, 32)` 作为数据源
- 面谈主题从 5 个预设主题循环取（6-8月服务季面谈 / 医疗险绩优面谈 / MBO面谈 / 月度业绩面谈 / 季度目标检视）
- 每行随机 1-3 个主题，面谈主题数量 = 待面谈数量（`pending`），多个主题用 `<br>` 分隔

**已移除的列：** 钻石等级、达钻差额（相比旧版）。

---

## 六、推荐问（Recommend Chips）

工件卡展示后，末尾追加快捷回复 chips（`appendRecChipsPC()`），引导用户继续操作（如"查看面谈对象详情"等）。

---

## 七、全局关键函数

| 函数 | 说明 |
|------|------|
| `routeQuery(query)` | 中央路由分发，解析用户输入并触发对应流程 |
| `appendUserBubble(text)` | 追加用户侧气泡，不触发 routeQuery |
| `appendInterviewFollowUp()` | 展示面谈月份选择卡（Step 1） |
| `window.intrSelectMonth(el, monthStr)` | 锁定月份选项，追加用户气泡，展开主题卡 |
| `appendInterviewThemeCard(msgs, monthStr)` | 展示面谈主题选择卡（Step 2） |
| `window.intrSelectTheme(el, theme, monthStr)` | 锁定主题选项，追加用户气泡，进入 AI 思考 |
| `appendInterviewArtifactFromFollowUp(monthStr, theme)` | 展示思考行 → AI 文案 + 工件卡 |
| `openDiamondWorkbench()` | 打开达钻潜力人员名单工作台 |
| `openInterviewWorkbench()` | 打开面谈对象工作台 |
| `openPolicyWorkbench()` | 打开承保代理人名单工作台 |
| `appendRecChipsPC()` | 追加推荐问 chips |
| `showToast(msg, duration)` | 底部 Toast 通知 |

---

## 八、数据源

```javascript
// 共用代理人数据（32条），字段说明：
var diamondAgentsData = [
  { name, outlet, dept, pVal, mVal, level, gap, gapPieces }
  // level: 钻石等级（如"金钻"、"银钻"等）
  // gap: FYC差额（元）
  // gapPieces: 件数差额
  // policyFyp / policyCount: 承保数据（仅承保工作台使用）
];
```

---

## 九、色彩规范（PC 端）

| Token | 值 | 用途 |
|---|---|---|
| Primary | `#2563eb` | 主色（PC端，区别于APP的#1976e8） |
| Text-secondary | `#64748b` | 表格数字、次级文本（待面谈数量等） |
| 钻石等级色 | 见 CLAUDE.md §十一 | 纯文字彩色，无背景 |
| 查看明细按钮 | `#2563eb` | border:none，hover 加下划线 |
| Sticky阴影 | `box-shadow:-2px 0 6px rgba(0,0,0,0.06)` | 固定列左侧分隔线 |
