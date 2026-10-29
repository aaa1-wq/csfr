# 数学分析 B：考试要求定理证明逐条讲解

> 说明：以下按照考试要求清单中的 18 个定理整理。附件主要提供定理名称和编号，个别定理的精确条件应以任课教师使用的教材版本为准。

## 一、上册

### 1．由闭区间套定理证明 Bolzano-Weierstrass 定理

#### 定理

有界数列必有收敛子列。

#### 证明

设数列 $\{x_n\}$ 有界，则存在闭区间 $I_1=[a_1,b_1]$，包含数列的所有项。

将 $I_1$ 二等分，至少有一个半区间包含数列的无穷多项，记为 $I_2$。继续进行，得到闭区间套：

$$
I_1\supset I_2\supset\cdots\supset I_k\supset\cdots
$$

并且：

$$
|I_k|=\frac{|I_1|}{2^{k-1}}\to0
$$

由闭区间套定理，存在唯一的 $\xi$，使得：

$$
\bigcap_{k=1}^{\infty}I_k=\{\xi\}
$$

依次选取 $n_1<n_2<\cdots$，使得 $x_{n_k}\in I_k$。由于 $\xi\in I_k$，有：

$$
|x_{n_k}-\xi|\le |I_k|\to0
$$

所以 $x_{n_k}\to\xi$，即数列存在收敛子列。

#### 思路

把有界数列转化为不断缩小的闭区间套，再从这些区间中选出下标递增的子列。

---

### 2．由 Bolzano-Weierstrass 定理证明 Cauchy 收敛原理

#### 定理

实数列收敛，当且仅当它是 Cauchy 数列。这里证明 Cauchy 数列必收敛。

#### 证明

设 $\{x_n\}$ 是 Cauchy 数列。取 $\varepsilon=1$，存在 $N$，使得 $m,n>N$ 时：

$$
|x_m-x_n|<1
$$

固定 $n=N+1$，则 $m>N$ 时：

$$
|x_m|\le |x_m-x_{N+1}|+|x_{N+1}|<1+|x_{N+1}|
$$

前 $N$ 项有限，所以整个数列有界。由 Bolzano-Weierstrass 定理，存在收敛子列 $x_{n_k}\to a$。

给定 $\varepsilon>0$，由 Cauchy 条件，存在 $N_1$，使得 $m,n>N_1$ 时：

$$
|x_m-x_n|<\frac{\varepsilon}{2}
$$

取 $k$ 足够大，使得 $n_k>N_1$ 且 $|x_{n_k}-a|<\frac{\varepsilon}{2}$。当 $n>N_1$ 时：

$$
|x_n-a|\le |x_n-x_{n_k}|+|x_{n_k}-a|<\varepsilon
$$

因此 $x_n\to a$。

#### 思路

$$
\text{Cauchy}\Rightarrow\text{有界}\Rightarrow\text{有收敛子列}\Rightarrow\text{整个数列收敛}
$$

---

### 3．Heine 定理

#### 定理

函数 $f$ 在 $x_0$ 连续，当且仅当对任意 $x_n\to x_0$，都有：

$$
f(x_n)\to f(x_0)
$$

#### 证明

若 $f$ 在 $x_0$ 连续，给定 $\varepsilon>0$，存在 $\delta>0$，使得：

$$
|x-x_0|<\delta\Rightarrow |f(x)-f(x_0)|<\varepsilon
$$

由于 $x_n\to x_0$，当 $n$ 足够大时 $|x_n-x_0|<\delta$，从而 $f(x_n)\to f(x_0)$。

反之，若 $f$ 在 $x_0$ 不连续，则存在 $\varepsilon_0>0$，使得对任意 $n$，存在 $x_n$ 满足：

$$
|x_n-x_0|<\frac1n，\qquad |f(x_n)-f(x_0)|\ge\varepsilon_0
$$

于是 $x_n\to x_0$，但 $f(x_n)$ 不趋于 $f(x_0)$，矛盾。

#### 思路

用数列语言刻画连续性；反证时令 $\delta=1/n$ 构造反例数列。

---

### 4．函数一致连续的充分必要条件

#### 定理

$f$ 在 $E$ 上一致连续，当且仅当对任意 $x_n,y_n\in E$，若：

$$
|x_n-y_n|\to0
$$

则：

$$
|f(x_n)-f(y_n)|\to0
$$

#### 证明

若 $f$ 一致连续，给定 $\varepsilon>0$，存在只依赖于 $\varepsilon$ 的 $\delta>0$，使得 $|x-y|<\delta$ 时：

$$
|f(x)-f(y)|<\varepsilon
$$

由于 $|x_n-y_n|\to0$，故最终有 $|f(x_n)-f(y_n)|<\varepsilon$。

反之，若不一致连续，则存在 $\varepsilon_0>0$，对每个 $n$ 可取 $x_n,y_n\in E$，使得：

$$
|x_n-y_n|<\frac1n，\qquad |f(x_n)-f(y_n)|\ge\varepsilon_0
$$

这与数列条件矛盾。

#### 思路

一致连续性等价于：任意两列点只要相互靠近，函数值就统一靠近。

---

### 5．Cantor 定理

#### 定理

连续函数在闭区间 $[a,b]$ 上一致连续。

#### 证明

反设 $f$ 不一致连续，则存在 $\varepsilon_0>0$ 以及 $x_n,y_n\in[a,b]$，使得：

$$
|x_n-y_n|<\frac1n，\qquad |f(x_n)-f(y_n)|\ge\varepsilon_0
$$

由 Bolzano-Weierstrass 定理，$\{x_n\}$ 有收敛子列 $x_{n_k}\to x_0\in[a,b]$。又有：

$$
|x_{n_k}-y_{n_k}|\to0
$$

故 $y_{n_k}\to x_0$。连续性给出：

$$
f(x_{n_k})\to f(x_0)，\qquad f(y_{n_k})\to f(x_0)
$$

于是 $|f(x_{n_k})-f(y_{n_k})|\to0$，矛盾。

#### 思路

闭区间的紧性保证可以选收敛子列，连续性再把两列的极限传递到函数值。

---

### 6．Leibniz 公式

#### 定理

$$
(uv)^{(n)}=\sum_{k=0}^{n}\binom{n}{k}u^{(k)}v^{(n-k)}
$$

#### 证明

当 $n=1$ 时，这是乘积求导法则：

$$
(uv)'=u'v+uv'
$$

假设结论对 $n$ 成立。求导得：

$$
(uv)^{(n+1)}
=\sum_{k=0}^{n}\binom{n}{k}
\left(u^{(k+1)}v^{(n-k)}+u^{(k)}v^{(n-k+1)}\right)
$$

合并同类项，并使用 Pascal 恒等式：

$$
\binom{n}{k-1}+\binom{n}{k}=\binom{n+1}{k}
$$

即可得到 $n+1$ 阶公式。

#### 思路

数学归纳法加乘积求导法则，二项式系数来自多次求导时的组合选择。

---

### 7．Lagrange 中值定理

#### 定理

若 $f$ 在 $[a,b]$ 上连续、在 $(a,b)$ 内可导，则存在 $\xi\in(a,b)$，使得：

$$
f'(\xi)=\frac{f(b)-f(a)}{b-a}
$$

#### 证明

构造：

$$
\varphi(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a)
$$

则：

$$
\varphi(a)=\varphi(b)=0
$$

由 Rolle 定理，存在 $\xi\in(a,b)$，使得 $\varphi'(\xi)=0$。而：

$$
\varphi'(x)=f'(x)-\frac{f(b)-f(a)}{b-a}
$$

所以得到结论。

#### 思路

构造辅助函数，把一般中值定理转化为 Rolle 定理。

---

### 8．微积分基本定理

#### 定理

若 $f$ 在 $[a,b]$ 上连续，定义：

$$
F(x)=\int_a^x f(t)\,dt
$$

则：

$$
F'(x)=f(x)
$$

#### 证明

由导数定义和定积分可加性：

$$
\frac{F(x+h)-F(x)}h=\frac1h\int_x^{x+h}f(t)\,dt
$$

由积分中值定理，存在 $\xi_h$ 位于 $x$ 与 $x+h$ 之间，使得：

$$
\frac1h\int_x^{x+h}f(t)\,dt=f(\xi_h)
$$

当 $h\to0$ 时，$\xi_h\to x$。由连续性，$f(\xi_h)\to f(x)$，故 $F'(x)=f(x)$。

#### 思路

先把导数商写成小区间上的平均值，再用积分中值定理和连续性取极限。

---

### 9．第二积分中值定理

#### 常见表述

若 $f$ 在 $[a,b]$ 上单调，$g$ 可积且不变号，则存在 $\xi\in[a,b]$，使得：

$$
\int_a^b f(x)g(x)\,dx
=f(a)\int_a^\xi g(x)\,dx
+f(b)\int_\xi^b g(x)\,dx
$$

#### 证明思路

令：

$$
G(x)=\int_a^x g(t)\,dt
$$

利用分部积分：

$$
\int_a^b f\,dG=f(b)G(b)-\int_a^bG\,df
$$

由于 $f$ 单调，$-df$ 不变号；由于 $g$ 不变号，$G$ 单调。再用连续函数关于单调权的积分中值性质，得到某个 $\xi$，使：

$$
\int_a^bG\,(-df)=G(\xi)(f(a)-f(b))
$$

整理即得结论。

#### 思路

分部积分把乘积积分转换为单调函数的加权平均。

---

## 二、下册

### 10．函数序列一致收敛的充分必要条件

#### 定理

$f_n$ 在 $E$ 上一致收敛，当且仅当对任意 $\varepsilon>0$，存在 $N$，使得 $m,n>N$ 时对所有 $x\in E$ 有：

$$
|f_n(x)-f_m(x)|<\varepsilon
$$

#### 证明

若 $f_n\rightrightarrows f$，则：

$$
|f_n-f_m|\le |f_n-f|+|f_m-f|<\varepsilon
$$

反之，对每个固定的 $x$，$\{f_n(x)\}$ 是实数 Cauchy 数列，因此定义：

$$
f(x)=\lim_{n\to\infty}f_n(x)
$$

令 $m\to\infty$，由一致 Cauchy 条件得到：

$$
|f_n(x)-f(x)|<\varepsilon
$$

且对所有 $x$ 同时成立，所以一致收敛。

#### 思路

把数列的 Cauchy 收敛原理逐点推广，并要求估计对所有 $x$ 统一成立。

---

### 11．函数序列一致收敛的连续性定理

#### 定理

若每个 $f_n$ 连续，且 $f_n$ 一致收敛于 $f$，则 $f$ 连续。

#### 证明

给定 $\varepsilon>0$，由一致收敛取 $N$，使得：

$$
|f(x)-f_N(x)|<\frac\varepsilon3
$$

对所有 $x$ 成立。由于 $f_N$ 连续，$x$ 接近 $x_0$ 时：

$$
|f_N(x)-f_N(x_0)|<\frac\varepsilon3
$$

于是：

$$
\begin{aligned}
|f(x)-f(x_0)|
&\le |f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|\\
&\quad+|f_N(x_0)-f(x_0)|<\varepsilon
\end{aligned}
$$

因此 $f$ 连续。

#### 思路

三项拆分：两端由一致收敛控制，中间由某个连续的 $f_N$ 控制。

---

### 12．Abel 第二定理

#### 定理

若 $\sum_{n=0}^{\infty}a_n=s$ 收敛，则：

$$
\lim_{x\to1^-}\sum_{n=0}^{\infty}a_nx^n=s
$$

#### 证明思路

令部分和：

$$
s_n=a_0+a_1+\cdots+a_n
$$

则 $a_n=s_n-s_{n-1}$。Abel 变换给出：

$$
\sum_{n=0}^{\infty}a_nx^n
=(1-x)\sum_{n=0}^{\infty}s_nx^n
$$

所以：

$$
\sum_{n=0}^{\infty}a_nx^n-s
=(1-x)\sum_{n=0}^{\infty}(s_n-s)x^n
$$

将右侧分为有限项和尾项。有限项前有因子 $1-x$，当 $x\to1^-$ 时趋于零；尾项利用 $s_n\to s$ 控制。因此整体趋于零。

#### 思路

用 Abel 变换把 $a_n$ 换成收敛的部分和 $s_n$，再进行有限项与尾项分解。

---

### 13．二次极限与二重极限的关系

#### 定理

若：

$$
\lim_{(x,y)\to(x_0,y_0)}f(x,y)=A
$$

且某个二次极限存在，则该二次极限也等于 $A$。例如：

$$
\lim_{x\to x_0}\left(\lim_{y\to y_0}f(x,y)\right)=A
$$

#### 证明思路

二重极限的定义保证当 $(x,y)$ 足够接近 $(x_0,y_0)$ 时：

$$
|f(x,y)-A|<\varepsilon
$$

先固定 $x$，令 $y\to y_0$，再令 $x\to x_0$，即可把该估计传递给二次极限。

#### 注意

二重极限存在通常可以推出已存在的二次极限等于它，但二次极限存在不一定能推出二重极限存在。

---

### 14．紧集上的连续映射一致连续

#### 定理

若 $K$ 是紧集，$f:K\to\mathbb R$ 连续，则 $f$ 在 $K$ 上一致连续。

#### 证明

反设不一致连续，则存在 $\varepsilon_0>0$ 以及 $x_n,y_n\in K$，使得：

$$
|x_n-y_n|<\frac1n，\qquad |f(x_n)-f(y_n)|\ge\varepsilon_0
$$

由紧性，$x_n$ 有收敛子列 $x_{n_k}\to x_0\in K$。由于 $|x_{n_k}-y_{n_k}|\to0$，所以 $y_{n_k}\to x_0$。连续性给出两列函数值都趋于 $f(x_0)$，从而差趋于零，矛盾。

#### 思路

紧性提供收敛子列，连续性把两列自变量的共同极限传递给函数值。

---

### 15．二元函数可微的充分条件

#### 定理

若 $f_x$、$f_y$ 在 $(x_0,y_0)$ 的邻域内存在，并且在该点连续，则 $f$ 在 $(x_0,y_0)$ 可微。

#### 证明

令 $\Delta x=x-x_0$，$\Delta y=y-y_0$。将增量拆开：

$$
\Delta f=f(x,y)-f(x_0,y)+f(x_0,y)-f(x_0,y_0)
$$

分别使用一元中值定理：

$$
f(x,y)-f(x_0,y)=f_x(x_0+\theta_1\Delta x,y)\Delta x
$$

$$
f(x_0,y)-f(x_0,y_0)=f_y(x_0,y_0+\theta_2\Delta y)\Delta y
$$

减去线性主部：

$$
f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y
$$

所得余项除以 $\sqrt{(\Delta x)^2+(\Delta y)^2}$ 后，由偏导数连续性趋于零。因此 $f$ 可微。

#### 思路

把二元增量拆成两次一元增量，再用一元中值定理估计余项。

---

### 16．混合导数相等的条件

#### 定理

若二阶混合偏导数在邻域内存在且连续，则：

$$
f_{xy}=f_{yx}
$$

#### 证明思路

考虑矩形增量：

$$
\Delta=f(x+h,y+k)-f(x+h,y)-f(x,y+k)+f(x,y)
$$

先沿 $x$ 方向作差，再沿 $y$ 方向作差，利用两次中值定理得到：

$$
\Delta=f_{xy}(\xi,\eta)hk
$$

若先沿 $y$ 再沿 $x$，则得到：

$$
\Delta=f_{yx}(\tilde\xi,\tilde\eta)hk
$$

令 $h,k\to0$，由混合偏导数连续性，两个表达式的极限相等，因此：

$$
f_{xy}(x,y)=f_{yx}(x,y)
$$

#### 思路

对同一个矩形增量使用两种求导顺序，最后令矩形缩小到一个点。

---

### 17．二元函数求导链式法则

#### 定理

若 $z=f(x,y)$，且 $x=x(t)$、$y=y(t)$，则：

$$
\frac{dz}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}
$$

#### 证明

由可微性：

$$
\Delta z=f_x\Delta x+f_y\Delta y+o\left(\sqrt{(\Delta x)^2+(\Delta y)^2}\right)
$$

又因为 $x(t)$、$y(t)$ 可导：

$$
\Delta x=x'(t)\Delta t+o(\Delta t)，\qquad \Delta y=y'(t)\Delta t+o(\Delta t)
$$

代入后除以 $\Delta t$，令 $\Delta t\to0$，得到：

$$
\frac{dz}{dt}=f_xx'(t)+f_yy'(t)
$$

#### 思路

总变化等于沿 $x$ 方向变化与沿 $y$ 方向变化之和。

---

### 18．二元函数的 Taylor 公式

#### 定理

若 $f$ 具有足够阶的连续偏导数，则：

$$
\begin{aligned}
f(x_0+h,y_0+k)
&=f(x_0,y_0)+f_x(x_0,y_0)h+f_y(x_0,y_0)k\\
&\quad+\frac12\left[f_{xx}(x_0,y_0)h^2+2f_{xy}(x_0,y_0)hk+f_{yy}(x_0,y_0)k^2\right]\\
&\quad+o(h^2+k^2)
\end{aligned}
$$

#### 证明

构造一元函数：

$$
\varphi(t)=f(x_0+th,y_0+tk)
$$

则：

$$
\varphi(0)=f(x_0,y_0)，\qquad \varphi(1)=f(x_0+h,y_0+k)
$$

由链式法则：

$$
\varphi'(0)=f_x(x_0,y_0)h+f_y(x_0,y_0)k
$$

再次求导：

$$
\varphi''(0)=f_{xx}h^2+2f_{xy}hk+f_{yy}k^2
$$

对 $\varphi$ 使用一元 Taylor 公式，即得到二元 Taylor 公式。

#### 思路

把二元函数沿连接 $(x_0,y_0)$ 与 $(x_0+h,y_0+k)$ 的直线限制成一元函数。

---

## 三、总复习：证明方法归类

### 1．反证法与反例数列

适用于 Heine 定理、一致连续判别法、Cantor 定理和紧集上的一致连续性。

典型结构：

$$
\text{否定结论}\Rightarrow\text{构造数列}\Rightarrow\text{取收敛子列}\Rightarrow\text{得到矛盾}
$$

### 2．闭区间套与紧性

适用于 Bolzano-Weierstrass 定理以及连续函数在紧集上的性质。

### 3．辅助函数法

适用于 Lagrange 中值定理。先构造满足端点条件的函数，再使用 Rolle 定理。

### 4．多元问题降为一元问题

适用于二元可微性、链式法则和 Taylor 公式。核心构造是：

$$
\varphi(t)=f(x_0+th,y_0+tk)
$$

### 5．有限项与尾项分解

适用于一致收敛和 Abel 第二定理。有限项直接估计，尾项利用极限或一致 Cauchy 条件控制。

### 6．考试书写建议

1. 先写清楚定理条件
2. 明确指出使用的定理，例如闭区间套定理、Bolzano-Weierstrass 定理或 Rolle 定理
3. 每次使用三角不等式时写出完整分解
4. 反证法要明确写出矛盾来自哪里
5. 多元证明中要说明固定了哪个变量，以及使用了一元中值定理的哪一部分
6. 结尾明确写出“因此定理得证”

