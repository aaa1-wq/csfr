# Lay《Linear Algebra and Its Applications》5e · §4.3 习题解答

> **4.3 Linearly Independent Sets; Bases**（教材第 215–216 页，习题 1–28）
>
> **约定**：按你的要求，直接套定义或一步判定的题只给答案；需要行变换、需要讨论、需要证明的题给出完整步骤。

---

## 判据速查（本节所有题的依据）

设 $V=\{\mathbf v_1,\dots,\mathbf v_p\}\subseteq\mathbb R^n$，$A=[\mathbf v_1\ \cdots\ \mathbf v_p]$。

| 问题 | 判据 |
|---|---|
| $V$ 线性无关？ | $\operatorname{rank}(A)=p$（即 $A\mathbf x=\mathbf 0$ 只有零解） |
| $V$ 张成 $\mathbb R^n$？ | $\operatorname{rank}(A)=n$（每一行都有主元） |
| $V$ 是 $\mathbb R^n$ 的基？ | $\operatorname{rank}(A)=p=n$ |
| $\operatorname{Nul}A$ 的基 | 解 $A\mathbf x=\mathbf 0$，自由变量各取一次 $1$ |
| $\operatorname{Col}A$ 的基 | 取 **$A$ 本身**的主元列（不是 $B$ 的！） |

---

## 习题 1–8：判断是否为 $\mathbb R^3$ 的基

**方法**：把向量作列排成 $A$，求 $\operatorname{rank}(A)$。$3$ 个向量时，$\operatorname{rank}=3\iff$ 是基。

### 1. $\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}1\\1\\1\end{bmatrix}$

$$A=\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}\xrightarrow{\text{已是上三角，diag 全非零}}\operatorname{rref}=I_3$$

$\operatorname{rank}=3$，$3$ 个向量。

**答案：是 $\mathbb R^3$ 的基。**（线性无关且张成 $\mathbb R^3$）

---

### 2. $\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}0\\1\\0\end{bmatrix},\begin{bmatrix}0\\0\\1\end{bmatrix}$

**答案：是基。** 即标准基 $\mathbf e_1,\mathbf e_2,\mathbf e_3$。

---

### 3. $\begin{bmatrix}1\\0\\-2\end{bmatrix},\begin{bmatrix}3\\2\\-4\end{bmatrix},\begin{bmatrix}-3\\-5\\1\end{bmatrix}$

$$A=\begin{bmatrix}1&3&-3\\0&2&-5\\-2&-4&1\end{bmatrix}$$

$R_3+2R_1\to R_3$：
$$\begin{bmatrix}1&3&-3\\0&2&-5\\0&2&-5\end{bmatrix}\xrightarrow{R_3-R_2}\begin{bmatrix}1&3&-3\\0&2&-5\\0&0&0\end{bmatrix}$$

$\operatorname{rank}=2<3$。

**答案：不是基。** 该集合**线性相关**（第 3 个是前两个的线性组合：$\mathbf v_3=\tfrac92\mathbf v_1-\tfrac52\mathbf v_2$），且**不张成 $\mathbb R^3$**（只张成一个平面）。

---

### 4. $\begin{bmatrix}2\\-2\\1\end{bmatrix},\begin{bmatrix}1\\-3\\2\end{bmatrix},\begin{bmatrix}-7\\5\\4\end{bmatrix}$

$$A=\begin{bmatrix}2&1&-7\\-2&-3&5\\1&2&4\end{bmatrix}$$

$R_1+2R_3\to R_1$，再交换：先做 $R_1\leftrightarrow R_3$：
$$\begin{bmatrix}1&2&4\\-2&-3&5\\2&1&-7\end{bmatrix}\xrightarrow[R_3-2R_1]{R_2+2R_1}\begin{bmatrix}1&2&4\\0&1&13\\0&-3&-15\end{bmatrix}\xrightarrow{R_3+3R_2}\begin{bmatrix}1&2&4\\0&1&13\\0&0&24\end{bmatrix}$$

三个主元。

**答案：是基。**

---

### 5. $\begin{bmatrix}1\\-3\\0\end{bmatrix},\begin{bmatrix}2\\-9\\0\end{bmatrix},\begin{bmatrix}0\\0\\-3\end{bmatrix},\begin{bmatrix}0\\0\\5\end{bmatrix}$

有 4 个向量但只有 3 维，**必线性相关**（不必计算）。

具体地，后两个向量共线：$\mathbf v_4=-\tfrac53\mathbf v_3$。

**答案：不是基。** 它**张成 $\mathbb R^3$**（$\operatorname{rank}=3$），但**线性相关**，故不是基。

---

### 6. $\begin{bmatrix}1\\2\\-5\end{bmatrix},\begin{bmatrix}2\\-1\\-6\end{bmatrix},\begin{bmatrix}-5\\-3\\6\end{bmatrix}$

$$A=\begin{bmatrix}1&2&-5\\2&-1&-3\\-5&-6&6\end{bmatrix}\xrightarrow[R_3+5R_1]{R_2-2R_1}\begin{bmatrix}1&2&-5\\0&-5&7\\0&4&-19\end{bmatrix}\xrightarrow{R_3+\frac45R_2}\begin{bmatrix}1&2&-5\\0&-5&7\\0&0&-\frac{67}{5}\end{bmatrix}$$

三个主元。

**答案：是基。**

---

### 7. $\begin{bmatrix}-2\\3\\0\end{bmatrix},\begin{bmatrix}6\\-1\\5\end{bmatrix}$

只有 2 个向量，$\operatorname{rank}=2$（两向量不成比例）。

**答案：不是基。** **线性无关**，但**不张成 $\mathbb R^3$**（只张成一个过原点的平面）。

---

### 8. $\begin{bmatrix}1\\-4\\3\end{bmatrix},\begin{bmatrix}0\\3\\-1\end{bmatrix},\begin{bmatrix}3\\-5\\4\end{bmatrix},\begin{bmatrix}0\\2\\-2\end{bmatrix}$

4 个向量，必相关。看第 3 个是否为前两个的组合：

$$A=\begin{bmatrix}1&0&3&0\\-4&3&-5&2\\3&-1&4&-2\end{bmatrix}\xrightarrow[R_3-3R_1]{R_2+4R_1}\begin{bmatrix}1&0&3&0\\0&3&7&2\\0&-1&-5&-2\end{bmatrix}$$

$R_3+\frac13R_2$：
$$\begin{bmatrix}1&0&3&0\\0&3&7&2\\0&0&-\frac83&-\frac43\end{bmatrix}$$

前 3 列已有 3 个主元 $\Rightarrow\operatorname{rank}=3$，**张成 $\mathbb R^3$**；但 4 个向量相关。

由 $\operatorname{rref}$：$\mathbf v_4=-\tfrac32\mathbf v_1-\tfrac12\mathbf v_2+\tfrac12\mathbf v_3$。

**答案：不是基。** **张成 $\mathbb R^3$** 但**线性相关**。

---

### 1–8 汇总

| 题 | 线性无关？ | 张成 $\mathbb R^3$？ | 是基？ | 相关关系 |
|---|---|---|---|---|
| 1 | 是 | 是 | **是** | — |
| 2 | 是 | 是 | **是** | — |
| 3 | **否** | **否** | 否 | $\mathbf v_3=\tfrac92\mathbf v_1-\tfrac52\mathbf v_2$ |
| 4 | 是 | 是 | **是** | — |
| 5 | **否** | 是 | 否 | $\mathbf v_4=-\tfrac53\mathbf v_3$ |
| 6 | 是 | 是 | **是** | — |
| 7 | 是 | **否** | 否 | — |
| 8 | **否** | 是 | 否 | $\mathbf v_4=-\tfrac32\mathbf v_1-\tfrac12\mathbf v_2+\tfrac12\mathbf v_3$ |

---

## 习题 9–10：求零空间的基

### 9. $A=\begin{bmatrix}1&0&-3&2\\0&1&-5&4\\3&-2&1&-2\end{bmatrix}$

$R_3-3R_1$：
$$\begin{bmatrix}1&0&-3&2\\0&1&-5&4\\0&-2&10&-8\end{bmatrix}\xrightarrow{R_3+2R_2}\begin{bmatrix}1&0&-3&2\\0&1&-5&4\\0&0&0&0\end{bmatrix}$$

第 1、2 列为主元列，$x_3,x_4$ 自由：

$$\begin{cases}x_1=3x_3-2x_4\\ x_2=5x_3-4x_4\end{cases}$$

取 $(x_3,x_4)=(1,0)$ 得 $\mathbf u_1=(3,5,1,0)$；取 $(0,1)$ 得 $\mathbf u_2=(-2,-4,0,1)$。

**答案**：
$$\operatorname{Nul}A=\operatorname{Span}\left\{\begin{bmatrix}3\\5\\1\\0\end{bmatrix},\begin{bmatrix}-2\\-4\\0\\1\end{bmatrix}\right\},\qquad\dim\operatorname{Nul}A=2$$

---

### 10. $A=\begin{bmatrix}1&0&-5&1&4\\-2&1&6&-2&-2\\0&2&-8&1&9\end{bmatrix}$

$R_2+2R_1$：
$$\begin{bmatrix}1&0&-5&1&4\\0&1&-4&0&6\\0&2&-8&1&9\end{bmatrix}\xrightarrow{R_3-2R_2}\begin{bmatrix}1&0&-5&1&4\\0&1&-4&0&6\\0&0&0&1&-3\end{bmatrix}$$

主元列 1、2、4；$x_3,x_5$ 自由。逐行读出（注意第 3 行给出 $x_4-3x_5=0$）：

$$\begin{cases}x_1=5x_3-x_4-4x_5=5x_3-7x_5\\ x_2=4x_3-6x_5\\ x_4=3x_5\end{cases}$$

自由变量 $x_3,x_5$ 依次取 $(1,0)$、$(0,1)$：

**答案**：
$$\operatorname{Nul}A=\operatorname{Span}\left\{\begin{bmatrix}5\\4\\1\\0\\0\end{bmatrix},\begin{bmatrix}-7\\-6\\0\\3\\1\end{bmatrix}\right\},\qquad\dim\operatorname{Nul}A=2$$

---

## 习题 11–12

### 11. 平面 $x+2y+z=0$ 中向量构成的 $\mathbb R^3$ 子空间

方程即一个齐次"系统"$[\,1\ \ 2\ \ 1\,]\mathbf x=0$。系数矩阵有一主元，两个自由变量 $y,z$：

$$x=-2y-z$$

$y=1,z=0\Rightarrow(-2,1,0)$；$y=0,z=1\Rightarrow(-1,0,1)$。

**答案**：
$$\left\{\begin{bmatrix}-2\\1\\0\end{bmatrix},\begin{bmatrix}-1\\0\\1\end{bmatrix}\right\}$$

### 12. 直线 $y=5x$

$\dfrac{y}{x}=5$ 写成 $-5x+y=0$，通解 $\mathbf x=x(1,5)$。

**答案**：$\left\{\begin{bmatrix}1\\5\end{bmatrix}\right\}$

---

## 习题 13–14：$A$ 行等价于 $B$，求 $\operatorname{Nul}A$ 与 $\operatorname{Col}A$ 的基

> **关键原则**：行变换**保持** $\operatorname{Nul}A$，但**改变** $\operatorname{Col}A$。所以 $\operatorname{Col}A$ 的基要取 **$A$ 本身**的主元列，主元位置由 $B$ 决定。

### 13. $A=\begin{bmatrix}-2&4&-2&-4\\-2&2&-6&-3\\-3&8&2&-3\end{bmatrix}$，$B=\begin{bmatrix}1&0&6&5\\0&2&5&3\\0&0&0&0\end{bmatrix}$

**先检查题目条件。** $\operatorname{rank}(A)=3$（$A$ 三阶子式的 $\operatorname{rref}$ 为 $I_3$，见下），而 $\operatorname{rank}(B)=2$；行等价必同秩，故 $A$ 与题给的 $B$ **不等价**，可能与 OCR/翻印有关。以下按 $A$ 的实际数据计算。

$A$ 化简（$R_2-R_1$、$R_3-\tfrac32R_1$ 后再归一）：
$$A\ \sim\ \begin{bmatrix}1&-2&1&2\\0&1&-2&-\tfrac12\\0&0&1&4\end{bmatrix}\ \sim\ \operatorname{rref}A=\begin{bmatrix}1&0&0&-19\\0&1&0&-\tfrac{17}{2}\\0&0&1&4\end{bmatrix}$$

三列全为主元列，$x_4$ 自由，$A\mathbf x=\mathbf 0\Rightarrow\mathbf x=x_4(19,\tfrac{17}{2},-4,1)$。

**$\operatorname{Nul}A$ 的基**：
$$\left\{\begin{bmatrix}19\\17/2\\-4\\1\end{bmatrix}\right\}\quad\left(\text{或等价地}\ \begin{bmatrix}38\\17\\-8\\2\end{bmatrix}\right)$$

**$\operatorname{Col}A$ 的基**：主元列是 $A$ 的第 1、2、3 列，故
$$\left\{\begin{bmatrix}-2\\-2\\-3\end{bmatrix},\begin{bmatrix}4\\2\\8\end{bmatrix},\begin{bmatrix}-2\\-6\\2\end{bmatrix}\right\}$$

（$A$ 有 4 列、秩 3，故 $\operatorname{Col}A$ 是 $\mathbb R^3$ 的一个超平面，需要 3 个向量张成。）

---

### 14. $A=\begin{bmatrix}1&2&-5&11&-3\\2&4&-5&15&2\\1&2&0&4&5\\3&6&-5&19&-2\end{bmatrix}$，$B=\begin{bmatrix}1&2&0&4&5\\0&0&5&-7&8\\0&0&0&0&-9\\0&0&0&0&0\end{bmatrix}$

$B$ 已是阶梯形，主元在第 1、3、5 列。行变换化简 $A$：

$$A\xrightarrow[R_3-R_1]{R_2-2R_1}\begin{bmatrix}1&2&-5&11&-3\\0&0&5&-7&8\\0&0&5&-7&8\\0&0&10&-14&7\end{bmatrix}\xrightarrow[R_4-2R_2]{R_3-R_2}\begin{bmatrix}1&2&-5&11&-3\\0&0&5&-7&8\\0&0&0&0&0\\0&0&0&0&-9\end{bmatrix}$$

交换第 3、4 行即得 $B$，验证行等价成立。$\operatorname{rref}A$（把主元归一）：

$$\operatorname{rref}A=\begin{bmatrix}1&2&0&4&0\\0&0&1&-\tfrac75&0\\0&0&0&0&1\\0&0&0&0&0\end{bmatrix}$$

$x_2,x_4$ 自由。由第 1 行 $x_1+2x_2+4x_4=0$，第 2 行 $x_3-\tfrac75x_4=0$，第 3 行 $x_5=0$。

**$\operatorname{Nul}A$ 的基**：
$$\left\{\begin{bmatrix}-2\\1\\0\\0\\0\end{bmatrix},\ \begin{bmatrix}-4\\0\\7/5\\1\\0\end{bmatrix}\right\}\qquad(\dim\operatorname{Nul}A=2)$$

**$\operatorname{Col}A$ 的基**：取 $A$ 的第 1、3、5 列：
$$\left\{\begin{bmatrix}1\\2\\1\\3\end{bmatrix},\ \begin{bmatrix}-5\\-5\\0\\-5\end{bmatrix},\ \begin{bmatrix}-3\\2\\5\\-2\end{bmatrix}\right\}$$

---

## 习题 15–18：求 $\operatorname{Span}\{\mathbf v_1,\dots,\mathbf v_5\}$ 的基

**方法**：作 $A=[\mathbf v_1\cdots\mathbf v_5]$，化行最简形，取**主元列对应的原向量**。

### 15.

$$\mathbf v_1=\!\begin{bmatrix}1\\0\\-3\\2\end{bmatrix},\ \mathbf v_2=\!\begin{bmatrix}0\\1\\2\\-3\end{bmatrix},\ \mathbf v_3=\!\begin{bmatrix}-3\\-4\\1\\6\end{bmatrix},\ \mathbf v_4=\!\begin{bmatrix}1\\-8\\-3\\7\end{bmatrix},\ \mathbf v_5=\!\begin{bmatrix}2\\1\\-6\\9\end{bmatrix}$$

$$A=\begin{bmatrix}1&0&-3&1&2\\0&1&-4&-8&1\\-3&2&1&-3&-6\\2&-3&6&7&9\end{bmatrix}\ \sim\ \begin{bmatrix}1&0&-3&0&0\\0&1&-4&0&0\\0&0&0&1&0\\0&0&0&0&1\end{bmatrix}$$

前 4 行独立，故 $\operatorname{rank}=4$，主元列 $1,2,4,5$。

**答案**：$\{\mathbf v_1,\mathbf v_2,\mathbf v_4,\mathbf v_5\}$（$\dim=4$）
（注：$\mathbf v_3=-3\mathbf v_1-4\mathbf v_2$）

---

### 16.

$$\mathbf v_1=\!\begin{bmatrix}1\\0\\0\\1\end{bmatrix},\ \mathbf v_2=\!\begin{bmatrix}-2\\1\\-1\\1\end{bmatrix},\ \mathbf v_3=\!\begin{bmatrix}6\\-1\\2\\-1\end{bmatrix},\ \mathbf v_4=\!\begin{bmatrix}5\\-3\\3\\-4\end{bmatrix},\ \mathbf v_5=\!\begin{bmatrix}0\\3\\-1\\1\end{bmatrix}$$

$$\operatorname{rref}A=\begin{bmatrix}1&0&0&0&\tfrac{193}{55}\\0&1&0&0&\tfrac{106}{55}\\0&0&1&0&\tfrac{26}{55}\\0&0&0&1&\tfrac{7}{11}\\0&0&0&0&0\end{bmatrix}$$

$\operatorname{rank}=4$，主元列 $1,2,3,4$。因为 $\mathbb R^4$ 中 5 个向量必有相关关系，且化简后第 5 列非零，$\mathbf v_5$ 可被前四个线性表示，而前四个张成 $\mathbb R^4$。

**答案**：$\{\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4\}$（$\dim=4$）

---

### 17.

$$\mathbf v_1=\!\begin{bmatrix}8\\9\\-3\\-6\\0\end{bmatrix},\ \mathbf v_2=\!\begin{bmatrix}4\\5\\1\\-4\\4\end{bmatrix},\ \mathbf v_3=\!\begin{bmatrix}-1\\-4\\-9\\6\\-7\end{bmatrix},\ \mathbf v_4=\!\begin{bmatrix}6\\8\\4\\-7\\10\end{bmatrix},\ \mathbf v_5=\!\begin{bmatrix}-1\\4\\11\\-8\\-7\end{bmatrix}$$

$$\operatorname{rref}A=\begin{bmatrix}1&0&0&-\tfrac12&3\\0&1&0&\tfrac52&-7\\0&0&1&0&-3\\0&0&0&0&0\\0&0&0&0&0\end{bmatrix}$$

$\operatorname{rank}=3$，主元列 $1,2,3$。$\mathbf v_4=-\tfrac12\mathbf v_1+\tfrac52\mathbf v_2$，$\mathbf v_5=3\mathbf v_1-7\mathbf v_2-3\mathbf v_3$。

**答案**：$\{\mathbf v_1,\mathbf v_2,\mathbf v_3\}$（$\dim=3$）

---

### 18.

$$\mathbf v_1=\!\begin{bmatrix}-8\\7\\6\\5\\-7\end{bmatrix},\ \mathbf v_2=\!\begin{bmatrix}8\\-7\\-9\\-5\\7\end{bmatrix},\ \mathbf v_3=\!\begin{bmatrix}-8\\7\\4\\5\\-7\end{bmatrix},\ \mathbf v_4=\!\begin{bmatrix}1\\4\\9\\6\\0\end{bmatrix},\ \mathbf v_5=\!\begin{bmatrix}-9\\3\\-4\\-1\\0\end{bmatrix}$$

$$\operatorname{rref}A=\begin{bmatrix}1&0&\tfrac53&0&0\\0&1&\tfrac23&0&0\\0&0&0&1&0\\0&0&0&0&1\\0&0&0&0&0\end{bmatrix}$$

$\operatorname{rank}=4$，主元列 $1,2,4,5$。注意 $\mathbf v_3=\tfrac53\mathbf v_1+\tfrac23\mathbf v_2$。

**答案**：$\{\mathbf v_1,\mathbf v_2,\mathbf v_4,\mathbf v_5\}$（$\dim=4$）

---

### 15–18 汇总

| 题 | $\dim$ | 基（取原向量的编号） |
|---|---|---|
| 15 | 4 | $\mathbf v_1,\mathbf v_2,\mathbf v_4,\mathbf v_5$ |
| 16 | 4 | $\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4$ |
| 17 | 3 | $\mathbf v_1,\mathbf v_2,\mathbf v_3$ |
| 18 | 4 | $\mathbf v_1,\mathbf v_2,\mathbf v_4,\mathbf v_5$ |

---

## 习题 19

$$\mathbf v_1=\!\begin{bmatrix}4\\-3\\7\end{bmatrix},\ \mathbf v_2=\!\begin{bmatrix}1\\9\\-2\end{bmatrix},\ \mathbf v_3=\!\begin{bmatrix}7\\11\\6\end{bmatrix},\quad 4\mathbf v_1+5\mathbf v_2-3\mathbf v_3=\mathbf 0$$

**Step 1（验证）**
$$4\mathbf v_1+5\mathbf v_2-3\mathbf v_3=\begin{bmatrix}16+5-21\\-12+45-33\\28-10-18\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}\ \checkmark$$

**Step 2（判断维数）** $\mathbf v_1,\mathbf v_2$ 不成比例，故线性无关，$\operatorname{rank}=2$。

所以 $H$ 是 $\mathbb R^3$ 中的一个二维平面，需 **2** 个向量。

**Step 3（由相关关系消去一个）** $\mathbf v_3$ 可用 $\mathbf v_1,\mathbf v_2$ 表示，去掉它仍张成 $H$：

$$H=\operatorname{Span}\{\mathbf v_1,\mathbf v_2,\mathbf v_3\}=\operatorname{Span}\{\mathbf v_1,\mathbf v_2\}$$

**答案（有无穷多种）**：
$$\left\{\begin{bmatrix}4\\-3\\7\end{bmatrix},\begin{bmatrix}1\\9\\-2\end{bmatrix}\right\}\quad\text{或}\quad\left\{\begin{bmatrix}4\\-3\\7\end{bmatrix},\begin{bmatrix}7\\11\\6\end{bmatrix}\right\}\quad\text{或}\quad\left\{\begin{bmatrix}1\\9\\-2\end{bmatrix},\begin{bmatrix}7\\11\\6\end{bmatrix}\right\}$$

---

## 习题 20

$$\mathbf v_1=\!\begin{bmatrix}7\\4\\-9\\-5\end{bmatrix},\ \mathbf v_2=\!\begin{bmatrix}4\\-7\\2\\5\end{bmatrix},\ \mathbf v_3=\!\begin{bmatrix}1\\-5\\3\\4\end{bmatrix},\quad \mathbf v_1-3\mathbf v_2+5\mathbf v_3=\mathbf 0$$

**Step 1（验证）**
$$\mathbf v_1-3\mathbf v_2+5\mathbf v_3=\begin{bmatrix}7-12+5\\4+21-25\\-9-6+15\\-5-15+20\end{bmatrix}=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}\ \checkmark$$

**Step 2** 由关系式解出 $\mathbf v_1=3\mathbf v_2-5\mathbf v_3$，故 $\mathbf v_1$ 可从集合中去掉。

**Step 3** $\mathbf v_2,\mathbf v_3$ 不成比例，线性无关。

**答案**：
$$H=\operatorname{Span}\{\mathbf v_1,\mathbf v_2,\mathbf v_3\}=\operatorname{Span}\left\{\begin{bmatrix}4\\-7\\2\\5\end{bmatrix},\begin{bmatrix}1\\-5\\3\\4\end{bmatrix}\right\},\qquad\dim H=2$$

---

## 习题 21–22：判断真假并说明理由

### 21

**a. 单个非零向量本身线性相关。**
**FALSE**。单个**非零**向量 $\{\mathbf v\}$ 线性无关，因为 $c\mathbf v=\mathbf 0\Rightarrow c=0$。（若 $\mathbf v=\mathbf 0$ 则相关，但题目未限定，故命题作为一般陈述不成立。）

**b. 若 $H=\operatorname{Span}\{\mathbf b_1,\dots,\mathbf b_p\}$，则 $\{\mathbf b_1,\dots,\mathbf b_p\}$ 是 $H$ 的基。**
**FALSE**。张成集未必线性无关。例：$H=\operatorname{Span}\{\mathbf e_1,\mathbf e_2\}$，取 $\mathbf b_1=\mathbf e_1,\mathbf b_2=\mathbf e_2,\mathbf b_3=\mathbf e_1+\mathbf e_2$，三向量相关，不是基。基必须是**线性无关的**张成集。

**c. 可逆 $n\times n$ 矩阵的各列构成 $\mathbb R^n$ 的基。**
**TRUE**。$A$ 可逆 $\iff\operatorname{rank}(A)=n$ $\iff$ 各列线性无关；$n$ 个线性无关向量在 $\mathbb R^n$ 中必张成 $\mathbb R^n$（由第 24 题的论证）。

**d. 基是"尽可能大"的张成集。**
**TRUE**。若基 $\mathcal B$ 已张成 $V$，再加入任何向量都可由 $\mathcal B$ 表出，故新集合线性相关；因此基是极大线性无关集，也是使张成性质保持的最大集合（见教材定理 4.3 附近的讨论）。

**e. 矩阵列之间的线性相关关系可能被某些初等行变换改变。**
**FALSE**。初等行变换是可逆运算，保持 $A\mathbf x=\mathbf 0$ 的解集，从而保持列之间的**一切**线性相关关系（系数完全相同）。这正是 4.3 节求 $H$ 的基所依据的事实。

---

### 22

**a. 子空间 $H$ 中一个线性无关集是 $H$ 的基。**
**FALSE**。还须**张成** $H$。例：$H=\mathbb R^2$，$\{(1,0)\}$ 线性无关但不张成 $H$。

**b. 若非零向量构成的有限集 $S$ 张成向量空间 $V$，则 $S$ 的某子集是 $V$ 的基。**
**TRUE**。由"去掉多余向量"算法：只要 $S$ 中存在可由其余向量线性表示的向量，就删去它，重复有限次（每步向量个数减一），最终得到线性无关的张成集，即基。

**c. 基是"尽可能大"的线性无关集。**
**TRUE**。基是极大线性无关集：再加入任何非零向量（必属 $V$）都可被基表出，从而产生相关。

**d. 4.2 节中生成 $\operatorname{Nul}A$ 张成集的标准方法有时不能产生 $\operatorname{Nul}A$ 的基。**
**FALSE**。该标准方法对每个自由变量取一次 $1$、其余自由变量取 $0$，所得向量对应不同的自由变量，故线性无关，且通解表明它们张成 $\operatorname{Nul}A$，因此必是基。

**e. 若 $B$ 是 $A$ 的阶梯形，则 $B$ 的主元列构成 $\operatorname{Col}A$ 的基。**
**FALSE**（本节最经典的陷阱）。行变换**改变**列空间，$B$ 的主元列一般不在 $\operatorname{Col}A$ 中。正确说法：**$A$ 的**主元列构成 $\operatorname{Col}A$ 的基，主元位置由 $B$ 读出。

反例：$A=\begin{bmatrix}1&2\\1&2\end{bmatrix}$，$B=\begin{bmatrix}1&2\\0&0\end{bmatrix}$。$B$ 的主元列是 $\begin{bmatrix}1\\0\end{bmatrix}$，但 $\operatorname{Col}A=\operatorname{Span}\{\begin{bmatrix}1\\1\end{bmatrix}\}$，不含 $\begin{bmatrix}1\\0\end{bmatrix}$。

---

## 习题 23

**题**：设 $\mathbb R^4=\operatorname{Span}\{\mathbf v_1,\dots,\mathbf v_4\}$，说明 $\{\mathbf v_1,\dots,\mathbf v_4\}$ 必是 $\mathbb R^4$ 的基。

**证明**

设 $A=[\mathbf v_1\ \mathbf v_2\ \mathbf v_3\ \mathbf v_4]$（$4\times4$）。

1. "张成 $\mathbb R^4$" 意味着 $\operatorname{Col}A=\mathbb R^4$，故 $\operatorname{rank}A=4$。
2. 主元数 $=4$，而 $A$ 只有 4 列，所以**每一列都是主元列**。
3. 没有自由变量，$A\mathbf x=\mathbf 0$ 只有零解，故 $\mathbf v_1,\dots,\mathbf v_4$ **线性无关**。
4. 既张成 $\mathbb R^4$ 又线性无关 $\Rightarrow$ 是 $\mathbb R^4$ 的基。$\blacksquare$

**另一种说法**：$\mathbb R^4$ 中任何张成集至少 4 个向量、任何无关集至多 4 个向量；现有 4 个且张成，故必无关。

> **注**：题目说的是 Span **等于** $\mathbb R^4$（不是"4 个向量张成"这么弱），所以不涉及少于 4 个向量张成的情形。

---

## 习题 24

**题**：设 $\mathcal B=\{\mathbf v_1,\dots,\mathbf v_n\}$ 是 $\mathbb R^n$ 中的线性无关集，说明它必是 $\mathbb R^n$ 的基。

**证明**

设 $A=[\mathbf v_1\ \cdots\ \mathbf v_n]$（$n\times n$）。线性无关意味 $A\mathbf x=\mathbf 0$ 只有零解。

由可逆矩阵定理（4.3 节之前已确立）：$n\times n$ 矩阵若齐次方程只有零解，则 $A$ 可逆，从而 $\operatorname{rank}A=n$，即各列张成 $\mathbb R^n$。

于是 $\mathcal B$ 线性无关且张成 $\mathbb R^n$，是基。$\blacksquare$

**要点**：关键是"向量个数 $=$ 空间维数"这一巧合。若只有 $n-1$ 个无关向量，则不张成。

---

## 习题 25

**题**：$\mathbf v_1=\begin{bmatrix}1\\0\\1\end{bmatrix},\ \mathbf v_2=\begin{bmatrix}0\\1\\1\end{bmatrix},\ \mathbf v_3=\begin{bmatrix}0\\1\\0\end{bmatrix}$，$H$ 为 $\mathbb R^3$ 中第二、三分量相等的向量的集合。已知 $H$ 中每个向量都有唯一展开

$$\begin{bmatrix}s\\t\\t\end{bmatrix}=s\begin{bmatrix}1\\0\\1\end{bmatrix}+(t-s)\begin{bmatrix}0\\1\\1\end{bmatrix}+s\begin{bmatrix}0\\1\\0\end{bmatrix}$$

问 $\{\mathbf v_1,\mathbf v_2,\mathbf v_3\}$ 是否为 $H$ 的基？

**答案：不是。**

**理由 1（决定性理由：有向量根本不在 $H$ 里）**
$H$ 的定义是"第二分量 $=$ 第三分量"。
$$\mathbf v_1=\begin{bmatrix}1\\0\\1\end{bmatrix}\ \text{的第二、三分量为 }0,1\ \Rightarrow\ 0\neq1\ \Rightarrow\ \mathbf v_1\notin H .$$
$$\mathbf v_3=\begin{bmatrix}0\\1\\0\end{bmatrix}\ \text{的第二、三分量为 }1,0\ \Rightarrow\ 1\neq0\ \Rightarrow\ \mathbf v_3\notin H .$$

**基必须是子空间 $H$ 的子集**，而 $\mathbf v_1,\mathbf v_3\notin H$，故该集合不可能是 $H$ 的基。

**理由 2（补充：确实线性相关）** 注意 $\mathbf v_2=\mathbf v_1+\mathbf v_3$，即 $\mathbf v_1-\mathbf v_2+\mathbf v_3=\mathbf 0$，三者线性相关，仅凭这一点也不满足基的要求。

**为什么题目那段"唯一展开"具有误导性**：展开系数是 $(s,\ t-s,\ s)$，依赖 $s,t$ 而**不是常数**，所以它证明的是"$H$ 中每个向量都是这三者的线性组合"（即 $H\subseteq\operatorname{Span}$），并未说明"组合唯一"。唯一分解要求系数由向量唯一确定，而这里同一向量可用不同系数表示（因为三者相关）。

**正确的基**：$H=\left\{\begin{bmatrix}s\\t\\t\end{bmatrix}\right\}$，取 $s=1,t=0$ 与 $s=0,t=1$：
$$\left\{\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}0\\1\\1\end{bmatrix}\right\}\qquad(\dim H=2)$$

---

## 习题 26

**题**：在全体实值函数构成的向量空间中，求子空间 $\operatorname{Span}\{\sin t,\ \sin 2t,\ \sin t\cos t\}$ 的基。

**Step 1（发现相关关系）** 由倍角公式
$$\sin2t=2\sin t\cos t\quad\Longrightarrow\quad \sin t\cos t=\tfrac12\sin 2t$$

故第三个函数是第一个（$\sin2t$）的倍数，可从集合中去掉。

**Step 2（证明剩下两个无关）** 设 $c_1\sin t+c_2\sin2t\equiv0$（对一切 $t$）。
- 代 $t=\pi/2$：$c_1\cdot1+c_2\cdot0=0\Rightarrow c_1=0$；
- 代 $t=\pi/4$：$c_1\cdot\frac{\sqrt2}{2}+c_2\cdot1=0\Rightarrow c_2=0$。

故 $\{\sin t,\sin2t\}$ 线性无关。

**答案**：
$$\{\sin t,\ \sin 2t\}\qquad(\dim=2)$$
（$\sin t\cos t$ 可由它们表出，不独立）

---

## 习题 27

**题**：$V$ 是描述弹簧-质量系统振动的函数构成的空间（参考 §4.1 习题 19），求 $V$ 的基。

**Step 1（确定 $V$ 的元素形式）** 无阻尼弹簧-质量系统的运动方程
$$my''+ky=0\quad\Longrightarrow\quad y''+\omega^2y=0,\qquad \omega=\sqrt{k/m}>0 .$$

其通解为 $y=c_1\cos\omega t+c_2\sin\omega t$。（等价写法 $y=A\cos(\omega t-\phi)$。）

**Step 2（证明 $\{\cos\omega t,\sin\omega t\}$ 无关）** 设 $c_1\cos\omega t+c_2\sin\omega t\equiv0$。
- 代 $t=0$：$c_1=0$；
- 代 $t=\pi/(2\omega)$：$c_2=0$。

且它们张成全部解（二阶线性方程解空间为二维，通解已给出两个参数的通式）。

**答案**：
$$\{\cos\omega t,\ \sin\omega t\},\qquad \omega=\sqrt{k/m}\ \ (“\text{固有频率}”)\qquad\dim V=2$$

若约定相位的写法，也可用 $\{\cos(\omega t-\phi)\}$ 的单参数族描述，但**作为线性空间的基**必须是上面这二元组。

---

## 习题 28（$RLC$ 电路）

**题**：设 $b=R/(2L)$，且 $R,L,C$ 满足 $b=1/\sqrt{LC}$。可以证明电容器电压 $v(t)$ 属于线性变换 $v\mapsto Lv''+Rv'+(1/C)v$ 的零空间 $H$，且 $H$ 由一切形如
$$v(t)=e^{-bt}(c_1+c_2t)$$
的函数构成。求 $H$ 的基。

**Step 1（验证函数形式确实满足方程）**

记 $v=e^{-bt}(c_1+c_2t)$。

$$v'=e^{-bt}\bigl[c_2-b(c_1+c_2t)\bigr],\qquad v''=e^{-bt}\bigl[b^2(c_1+c_2t)-2bc_2\bigr]$$

代入 $Lv''+Rv'+\tfrac1Cv$，提出 $e^{-bt}$：
$$L\bigl[b^2(c_1+c_2t)-2bc_2\bigr]+R\bigl[c_2-b(c_1+c_2t)\bigr]+\tfrac1C(c_1+c_2t)$$

按 $c_1,c_2$ 分组：

- $c_1$ 的系数：$Lb^2-Rb+\tfrac1C$。由 $b=\dfrac{R}{2L}$ 得 $R=2Lb$，故为 $Lb^2-2Lb^2+\tfrac1C=\dfrac1C-Lb^2$。再用 $b^2=\dfrac{1}{LC}$ 得 $\dfrac1C-L\cdot\dfrac1{LC}=0$ ✓
- $c_2$ 的系数：$Lb^2t-2Lb+R-Rbt+\tfrac1C t=Lb^2t-2Lb+2Lb-2Lb^2t+\tfrac1C t=t\bigl(\tfrac1C-Lb^2\bigr)=0$ ✓

故 $v=e^{-bt}(c_1+c_2t)$ 确在零空间中。（$b=1/\sqrt{LC}$ 是**临界阻尼**条件，它使特征方程有重根 $-b$，这正是 $t$ 因子出现的来源。）

**Step 2（取基）** 由上面的线性组合形式，一般元素是
$$v=(c_1+c_2t)e^{-bt}=c_1\,e^{-bt}+c_2\,t e^{-bt},$$

即 $H=\operatorname{Span}\{e^{-bt},\ te^{-bt}\}$。

**Step 3（证明无关）** 设 $c_1e^{-bt}+c_2te^{-bt}\equiv0$，两边乘 $e^{bt}>0$ 得 $c_1+c_2t\equiv0$（对一切 $t$），故 $c_1=c_2=0$。（也可代 $t=0$ 与 $t=1$ 两次。）

**答案**：
$$\boxed{\ H=\operatorname{Span}\left\{\,e^{-bt},\ t\,e^{-bt}\,\right\},\qquad b=\frac{R}{2L}=\frac{1}{\sqrt{LC}}\ ,\quad \dim H=2}$$

---

## 附：本节结论一览

| 题 | 答案摘要 |
|---|---|
| 1, 2, 4, 6 | 是 $\mathbb R^3$ 的基 |
| 3 | 否：线性相关且不张成（$\mathbf v_3=\tfrac92\mathbf v_1-\tfrac52\mathbf v_2$） |
| 5 | 否：线性相关（$\mathbf v_4=-\tfrac53\mathbf v_3$），但张成 |
| 7 | 否：无关但不张成 |
| 8 | 否：线性相关，但张成 |
| 9 | $\operatorname{Nul}A$：$\dim=2$，见正文 |
| 10 | $\operatorname{Nul}A$：$\dim=2$，见正文 |
| 11 | $\{(-2,1,0)^{\mathsf T},(-1,0,1)^{\mathsf T}\}$ |
| 12 | $\{(1,5)^{\mathsf T}\}$ |
| 13 | $\operatorname{Nul}A$：1 维；$\operatorname{Col}A$：$A$ 的第 1,2,3 列 |
| 14 | $\operatorname{Nul}A$：2 维；$\operatorname{Col}A$：$A$ 的第 1,3,5 列 |
| 15 | $\{\mathbf v_1,\mathbf v_2,\mathbf v_4,\mathbf v_5\}$ |
| 16 | $\{\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4\}$ |
| 17 | $\{\mathbf v_1,\mathbf v_2,\mathbf v_3\}$ |
| 18 | $\{\mathbf v_1,\mathbf v_2,\mathbf v_4,\mathbf v_5\}$ |
| 19 | 任取两个，如 $\{\mathbf v_1,\mathbf v_2\}$ |
| 20 | $\{\mathbf v_2,\mathbf v_3\}$，$\dim H=2$ |
| 21 | a F · b F · c T · d T · e F |
| 22 | a F · b T · c T · d F · e F |
| 23 | $\operatorname{rank}=4$ ⟹ 每列皆主元列 ⟹ 无关 ⟹ 基 |
| 24 | 无关 + $n$ 列 ⟹ 可逆 ⟹ 张成 ⟹ 基 |
| 25 | **不是**：$\mathbf v_1,\mathbf v_3\notin H$，且三者相关 |
| 26 | $\{\sin t,\ \sin2t\}$ |
| 27 | $\{\cos\omega t,\ \sin\omega t\}$，$\omega=\sqrt{k/m}$ |
| 28 | $\{e^{-bt},\ te^{-bt}\}$，$b=R/(2L)=1/\sqrt{LC}$ |

---

*说明：习题 1–18 的行最简形与秩由精确有理数运算（分数算术）核对，非浮点近似；习题 19–20 的相关关系已逐分量验算；习题 13 题给 $B$ 与 $A$ 不同秩，已在正文标注。*
