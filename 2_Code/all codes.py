#!/usr/bin/env python
# coding: utf-8

# In[1]:


from astroquery.mast import Observations


# In[2]:


from astropy.io import fits

file = r"C:\Users\21665\Desktop\kepler17\fits\kplr010619192-2009166043257_llc.fits"

hdul = fits.open(file)

hdul.info()
data = hdul[1].data

print(data.columns)


# In[6]:


import glob

files = sorted(
    glob.glob(
        r"C:\Users\21665\Desktop\kepler17\fits\*.fits"
    )
)

for f in files:
    print(f)


# In[12]:


import numpy as np
from astropy.io import fits
import glob

files = sorted(
    glob.glob(
        r"C:\Users\21665\Desktop\kepler17\fits\*.fits"
    )
)

time_all = []
flux_all = []
err_all = []

for file in files:

    with fits.open(file) as hdul:

        data = hdul[1].data

        time_all.append(data["TIME"])
        flux_all.append(data["PDCSAP_FLUX"])
        err_all.append(data["PDCSAP_FLUX_ERR"])

time = np.concatenate(time_all)
flux = np.concatenate(flux_all)
err = np.concatenate(err_all)
print(len(time))
print(len(flux))
print(len(err))
print(time[:10])
print(flux[:10])
print(time.shape)
print(flux.shape)
for f in files:
    print(f)


# In[13]:


import pandas as pd

df = pd.DataFrame({
    "time": time,
    "flux": flux,
    "flux_err": err
})

df.to_csv(
    r"C:\Users\21665\Desktop\kepler17\Kepler17_Q1_Q4.csv",
    index=False
)


# In[16]:


import pandas as pd
import numpy as np

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_Q1_Q4.csv"

df = pd.read_csv(file)

print(df.head())
print(df.shape)


# In[17]:


import pandas as pd
import numpy as np

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_Q1_Q4.csv"

df = pd.read_csv(file)

median_flux = np.median(df["flux"])

df["flux_norm"] = df["flux"] / median_flux

df["flux_err_norm"] = df["flux_err"] / median_flux

print(df.head())
output_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_Q1_Q4_normalized.csv"

df.to_csv(
    output_file,
    index=False
)

print("保存成功：", output_file)


# In[18]:


print(df["flux"].isna().sum())
print(df["flux_err"].isna().sum())
print(df["flux"].describe())
print(np.median(df["flux"]))


# In[20]:


import pandas as pd
import numpy as np

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_Q1_Q4.csv"

df = pd.read_csv(file)

print("原始数据点数:", len(df))

df = df.dropna(
    subset=["time","flux","flux_err"]
)

print("清洗后数据点数:", len(df))
median_flux = np.median(df["flux"])

print("Median Flux =", median_flux)

df["flux_norm"] = df["flux"] / median_flux

df["flux_err_norm"] = df["flux_err"] / median_flux
print(df.head())
output_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_clean.csv"

df.to_csv(
    output_file,
    index=False
)

print("保存成功")


# In[2]:


# ============================================
# Figure 1. Kepler-17 Light Curve (Q1-Q4)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 读取数据
# -----------------------------
file = r"C:\Users\21665\Desktop\kepler17\Kepler17_clean.csv"

df = pd.read_csv(file)

# -----------------------------
# 提取数据
# -----------------------------
time = df["time"].values
flux = df["flux_norm"].values
flux_err = df["flux_err_norm"].values

# -----------------------------
# 绘制 Light Curve
# -----------------------------
plt.figure(figsize=(14,5))

plt.scatter(
    time,
    flux,
    s=1,
    color="black",
    alpha=0.6
)

plt.xlabel("Time (BJD - 2454833)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title("Kepler-17 Light Curve (Q1-Q4)", fontsize=15)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# In[4]:


# ============================================
# Figure 1. Raw Kepler-17 Light Curve
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
file = r"C:\Users\21665\Desktop\kepler17\Kepler17_clean.csv"
df = pd.read_csv(file)

# 提取数据
time = df["time"].values
flux = df["flux"].values

# 设置绘图参数
plt.figure(figsize=(14,5), dpi=150)

# 绘制散点
plt.scatter(
    time,
    flux,
    s=1,
    c="black",
    alpha=0.6,
    rasterized=True
)

# 坐标轴
plt.xlabel("Time (BJD - 2454833)", fontsize=13)
plt.ylabel(r"Flux ($e^{-}\,\mathrm{s}^{-1}$)", fontsize=13)

plt.title("Raw Kepler-17 Light Curve (Q1–Q4)", fontsize=15)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# In[5]:


# ============================================
# Figure 1. Raw Kepler-17 Light Curve
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
file = r"C:\Users\21665\Desktop\kepler17\Kepler17_clean.csv"
df = pd.read_csv(file)

# 提取数据
time = df["time"].values
flux = df["flux"].values

# 设置画布
plt.figure(figsize=(14,5), dpi=150)

# 用折线连接所有数据点
plt.plot(
    time,
    flux,
    color="royalblue",
    linewidth=0.6,
    label="Light Curve"
)

# 再叠加观测点（可选）
plt.scatter(
    time,
    flux,
    s=3,
    color="black",
    alpha=0.5,
    label="Observations"
)

plt.xlabel("Time (BJD - 2454833)", fontsize=13)
plt.ylabel(r"Flux ($e^{-}\,\mathrm{s}^{-1}$)", fontsize=13)
plt.title("Raw Kepler-17 Light Curve (Q1–Q4)", fontsize=15)

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
plt.figure(figsize=(14,5), dpi=150)

plt.plot(
    time,
    flux,
    color="black",
    linewidth=0.5
)

plt.xlabel("Time (BJD - 2454833)")
plt.ylabel(r"Flux ($e^{-}\,\mathrm{s}^{-1}$)")
plt.title("Raw Kepler-17 Light Curve (Q1–Q4)")

plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# In[6]:


# ============================================
# Quarter-by-Quarter Normalization for Kepler-17
# ============================================

import pandas as pd
import numpy as np

# --------------------------------------------
# 读取CSV
# --------------------------------------------
input_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_clean.csv"

df = pd.read_csv(input_file)

# --------------------------------------------
# 根据时间自动划分Quarter
# (Q1~Q4，对应你下载的四个季度)
# --------------------------------------------

conditions = [
    (df["time"] < 165),
    (df["time"] >= 165) & (df["time"] < 260),
    (df["time"] >= 260) & (df["time"] < 355),
    (df["time"] >= 355)
]

quarters = ["Q1", "Q2", "Q3", "Q4"]

df["quarter"] = np.select(conditions, quarters, default="Unknown")

# --------------------------------------------
# 创建新的列
# --------------------------------------------

df["flux_norm"] = np.nan
df["flux_err_norm"] = np.nan

# --------------------------------------------
# 对每个Quarter分别归一化
# --------------------------------------------

for q in quarters:

    mask = df["quarter"] == q

    median_flux = np.median(df.loc[mask, "flux"])

    print(f"{q}: median flux = {median_flux:.3f}")

    df.loc[mask, "flux_norm"] = (
        df.loc[mask, "flux"] / median_flux
    )

    df.loc[mask, "flux_err_norm"] = (
        df.loc[mask, "flux_err"] / median_flux
    )

# --------------------------------------------
# 保存新的CSV
# --------------------------------------------

output_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_quarter_normalized.csv"

df.to_csv(output_file, index=False)

print("\n保存完成！")
print(output_file)


# In[7]:


# ============================================
# Figure 1. Kepler-17 Light Curve (Q1-Q4)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 读取数据
# -----------------------------
file = r"C:\Users\21665\Desktop\kepler17\Kepler17_quarter_normalized.csv"

df = pd.read_csv(file)

# -----------------------------
# 提取数据
# -----------------------------
time = df["time"].values
flux = df["flux_norm"].values
flux_err = df["flux_err_norm"].values

# -----------------------------
# 绘制 Light Curve
# -----------------------------
plt.figure(figsize=(14,5))

plt.scatter(
    time,
    flux,
    s=1,
    color="black",
    alpha=0.6
)

plt.xlabel("Time (BJD - 2454833)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title("Kepler-17 Light Curve (Q1-Q4)", fontsize=15)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# In[8]:


# ============================================
# Publication-style Light Curve
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_quarter_normalized.csv"
df = pd.read_csv(file)

plt.figure(figsize=(14,5), dpi=150)

for q in ["Q1", "Q2", "Q3", "Q4"]:
    sub = df[df["quarter"] == q]

    plt.plot(
        sub["time"],
        sub["flux_norm"],
        color="black",
        linewidth=0.5
    )

plt.xlabel("Time (BJD - 2454833)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)
plt.title("Kepler-17 Light Curve (Q1–Q4)", fontsize=15)

plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()


# In[10]:


# ==========================================================
# Kepler-17 Light Curve Detrending (Flatten)
# ==========================================================

import lightkurve as lk
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# 1. 读取数据
# ==========================================================

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_quarter_normalized.csv"

df = pd.read_csv(file)

# ==========================================================
# 2. 构造 LightCurve
# ==========================================================

lc = lk.LightCurve(
    time=df["time"].values,
    flux=df["flux_norm"].values
)

print(lc)

# ==========================================================
# 3. 去趋势
# ==========================================================

lc_flat = lc.flatten(
    window_length=901,
    polyorder=2
)

# ==========================================================
# 4. 去除异常值
# ==========================================================

lc_flat = lc_flat.remove_outliers(
    sigma=5
)

# ==========================================================
# 5. 绘图
# ==========================================================

plt.figure(figsize=(14,5), dpi=150)

plt.plot(
    lc_flat.time.value,
    lc_flat.flux.value,
    color="black",
    linewidth=0.5
)

plt.xlabel("Time (BJD - 2454833)", fontsize=13)
plt.ylabel("Flattened Flux", fontsize=13)
plt.title("Flattened Kepler-17 Light Curve", fontsize=15)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

# ==========================================================
# 6. 保存CSV
# ==========================================================

flat_df = pd.DataFrame({
    "time": lc_flat.time.value,
    "flux_flat": lc_flat.flux.value
})

output = r"C:\Users\21665\Desktop\kepler17\Kepler17_flatten.csv"

flat_df.to_csv(
    output,
    index=False
)

print("===================================")
print("Flattened light curve saved to:")
print(output)
print("===================================")


# In[11]:


# ==========================================================
# Kepler-17 Transit Search using Box Least Squares (BLS)
# ==========================================================

import lightkurve as lk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. Read flattened light curve
# ==========================================================

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_flatten.csv"

df = pd.read_csv(file)

lc = lk.LightCurve(
    time=df["time"].values,
    flux=df["flux_flat"].values
)

print("--------------------------------")
print("Light Curve Loaded")
print(lc)
print("--------------------------------")

# ==========================================================
# 2. Create BLS Periodogram
# ==========================================================

print("Running BLS search...")

period = np.linspace(
    1,
    20,
    10000
)

bls = lc.to_periodogram(
    method="bls",
    period=period,
    frequency_factor=100
)

print("BLS Finished!")

# ==========================================================
# 3. Plot BLS Periodogram
# ==========================================================

plt.figure(figsize=(10,5), dpi=150)

plt.plot(
    bls.period.value,
    bls.power.value,
    color="black",
    linewidth=1
)

plt.xlabel("Period (days)", fontsize=13)
plt.ylabel("BLS Power", fontsize=13)

plt.title("Figure 3. BLS Periodogram of Kepler-17", fontsize=15)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

# ==========================================================
# 4. Best-fit Transit Parameters
# ==========================================================

planet_period = bls.period_at_max_power
planet_t0 = bls.transit_time_at_max_power
planet_duration = bls.duration_at_max_power

print("\n===================================")
print("Best Transit Parameters")
print("===================================")

print(f"Orbital Period  = {planet_period}")
print(f"Transit Epoch   = {planet_t0}")
print(f"Transit Duration= {planet_duration}")

print("===================================\n")

# ==========================================================
# 5. Phase Fold
# ==========================================================

folded = lc.fold(
    period=planet_period,
    epoch_time=planet_t0
)

# ==========================================================
# 6. Plot Folded Transit
# ==========================================================

plt.figure(figsize=(8,5), dpi=150)

plt.scatter(
    folded.time.value,
    folded.flux.value,
    s=2,
    color="black",
    alpha=0.5
)

plt.xlabel("Phase (days)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title("Figure 4. Phase-folded Transit of Kepler-17b", fontsize=15)

plt.xlim(-0.2,0.2)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

# ==========================================================
# 7. Save folded light curve
# ==========================================================

fold_df = pd.DataFrame({

    "phase": folded.time.value,

    "flux": folded.flux.value

})

output = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_folded.csv"

fold_df.to_csv(
    output,
    index=False
)

print("Phase-folded light curve saved!")

print(output)

# ==========================================================
# 8. Transit Model
# ==========================================================

planet_model = bls.get_transit_model(
    period=planet_period,
    transit_time=planet_t0,
    duration=planet_duration
)

plt.figure(figsize=(8,5), dpi=150)

ax = plt.gca()

plt.scatter(
    folded.time.value,
    folded.flux.value,
    s=2,
    color="black",
    alpha=0.4,
    label="Kepler Data"
)

planet_model.fold(
    period=planet_period,
    epoch_time=planet_t0
).plot(
    ax=ax,
    color="red",
    linewidth=2,
    label="BLS Model"
)

plt.xlim(-0.2,0.2)

plt.xlabel("Phase (days)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title("Figure 5. BLS Transit Model", fontsize=15)

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

# ==========================================================
# 9. Transit Mask
# ==========================================================

planet_mask = bls.get_transit_mask(
    period=planet_period,
    transit_time=planet_t0,
    duration=planet_duration
)

masked_lc = lc[~planet_mask]

plt.figure(figsize=(14,5), dpi=150)

plt.scatter(
    masked_lc.time.value,
    masked_lc.flux.value,
    s=1,
    color="black",
    label="Out of Transit"
)

plt.scatter(
    lc[planet_mask].time.value,
    lc[planet_mask].flux.value,
    s=5,
    color="red",
    label="Transit"
)

plt.xlabel("Time (days)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title("Figure 6. Transit Cadence Mask", fontsize=15)

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

print("\nAnalysis Completed Successfully!")


# In[3]:


# ==========================================================
# Kepler-17 Phase Fold Analysis
# ==========================================================

import lightkurve as lk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. Read Flattened Light Curve
# ==========================================================

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_flatten.csv"

df = pd.read_csv(file)

lc = lk.LightCurve(
    time=df["time"].values,
    flux=df["flux_flat"].values
)

print("--------------------------------")
print("Light Curve Loaded")
print("--------------------------------")
print(lc)

# ==========================================================
# 2. BLS Search
# ==========================================================

print("\nRunning BLS Search...\n")

period = np.linspace(
    1,
    20,
    10000
)

bls = lc.to_periodogram(
    method="bls",
    period=period,
    frequency_factor=100
)

print("BLS Search Finished!")

# ==========================================================
# 3. Best Parameters
# ==========================================================

planet_period = bls.period_at_max_power
planet_t0 = bls.transit_time_at_max_power
planet_duration = bls.duration_at_max_power

print("\n==============================")
print("Best-fit Transit Parameters")
print("==============================")

print(f"Orbital Period  : {planet_period}")
print(f"Transit Epoch   : {planet_t0}")
print(f"Transit Duration: {planet_duration}")

print("==============================")

# ==========================================================
# 4. Phase Fold
# ==========================================================

folded = lc.fold(
    period=planet_period,
    epoch_time=planet_t0
)

# ==========================================================
# 5. Figure 4
# Raw Phase-folded Light Curve
# ==========================================================

plt.figure(figsize=(8,5), dpi=150)

plt.scatter(
    folded.time.value,
    folded.flux.value,
    s=2,
    color="black",
    alpha=0.4
)

plt.xlabel("Phase (days)", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title(
    "Figure 4. Phase-folded Transit of Kepler-17b",
    fontsize=15
)

plt.grid(alpha=0.3)

plt.xlim(-0.2,0.2)

plt.tight_layout()

plt.show()

# ==========================================================
# 6. Figure 5
# Phase Fold + Binned Flux
# ==========================================================

fig, ax = plt.subplots(figsize=(8,5), dpi=150)

# 原始散点
ax.scatter(
    folded.time.value,
    folded.flux.value,
    s=2,
    color="gray",
    alpha=0.25,
    label="Kepler Data"
)

# Binned 数据
binned = folded.bin(
    time_bin_size=0.005
)

ax.plot(
    binned.time.value,
    binned.flux.value,
    color="red",
    linewidth=2,
    label="Binned Flux"
)

ax.set_xlim(-0.2,0.2)

ax.set_xlabel("Phase (days)", fontsize=13)
ax.set_ylabel("Normalized Flux", fontsize=13)

ax.set_title(
    "Figure 5. Phase-folded Transit (Binned)",
    fontsize=15
)

ax.grid(alpha=0.3)

ax.legend()

plt.tight_layout()

plt.show()

# ==========================================================
# 7. Save Folded Data
# ==========================================================

phase_df = pd.DataFrame({

    "phase": folded.time.value,

    "flux": folded.flux.value

})

output = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_folded.csv"

phase_df.to_csv(
    output,
    index=False
)

print("\nPhase-folded data saved to:")

print(output)

# ==========================================================
# 8. Save Binned Data
# ==========================================================

binned_df = pd.DataFrame({

    "phase": binned.time.value,

    "flux": binned.flux.value

})

output2 = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_binned.csv"

binned_df.to_csv(
    output2,
    index=False
)

print("\nBinned phase curve saved to:")

print(output2)

print("\nAnalysis Completed Successfully!")


# In[6]:


pip install batman-package


# In[7]:


# ==========================================================
# Figure 6
# Kepler-17b Phase-folded Transit
# Literature Batman Model vs Observed Data
# ==========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import batman

# ==========================================================
# Read phase-folded observational data
# ==========================================================

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_binned.csv"

df = pd.read_csv(file)

phase = df["phase"].values
flux = df["flux"].values

# ==========================================================
# Literature parameters (Kepler-17b)
# Désert et al. (2011)
# ==========================================================

params = batman.TransitParams()

params.t0 = 0.0              # Mid-transit

params.per = 1.4857108       # days

params.rp = 0.1302           # Rp/R*

params.a = 5.73              # a/R*

params.inc = 89.1            # degree

params.ecc = 0.0

params.w = 90.0

params.u = [0.35, 0.25]

params.limb_dark = "quadratic"

# ==========================================================
# Generate theoretical model
# ==========================================================

# Phase (-0.2~0.2 day)

t = np.linspace(-0.2, 0.2, 2000)

m = batman.TransitModel(params, t)

model_flux = m.light_curve(params)

# ==========================================================
# Plot
# ==========================================================

plt.figure(figsize=(10,6))

# ------------------------------------------
# Observational data
# ------------------------------------------

plt.scatter(
    phase,
    flux,
    s=18,
    color="gray",
    alpha=0.7,
    label="Kepler Observation"
)

# ------------------------------------------
# Batman model
# ------------------------------------------

plt.plot(
    t,
    model_flux,
    color="red",
    linewidth=3,
    label="Batman Model (Literature Parameters)"
)

# ------------------------------------------

plt.xlabel("Phase (days)", fontsize=14)

plt.ylabel("Normalized Flux", fontsize=14)

plt.title(
    "Figure 6. Kepler-17b Transit: Observation vs Batman Model",
    fontsize=16
)

plt.xlim(-0.2,0.2)

plt.grid(alpha=0.3)

plt.legend(fontsize=12)

plt.tight_layout()

plt.show()


# In[8]:


pip install emcee batman-package corner


# In[4]:


# ============================================================
# Step 2
# MCMC fitting of Kepler-17b transit
# Batman + emcee
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import batman
import emcee
import corner

# ============================================================
# Read phase-folded data
# ============================================================

file = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_binned.csv"

df = pd.read_csv(file)

phase = df["phase"].values
flux = df["flux"].values

# 假设误差统一
flux_err = np.ones_like(flux)*0.0005

# ============================================================
# Fixed Parameters
# ============================================================

P = 1.4857108
t0 = 0.0

ecc = 0.0
w = 90.

u = [0.47,0.14]

# ============================================================
# Batman Model
# ============================================================

def transit_model(theta):

    rp, a, inc = theta

    params = batman.TransitParams()

    params.t0 = t0
    params.per = P

    params.rp = rp
    params.a = a
    params.inc = inc

    params.ecc = ecc
    params.w = w

    params.u = u
    params.limb_dark = "quadratic"

    m = batman.TransitModel(
        params,
        phase
    )

    return m.light_curve(params)

# ============================================================
# Prior
# ============================================================

def log_prior(theta):

    rp,a,inc = theta

    if 0.05<rp<0.20 and \
       3<a<8 and \
       80<inc<90:

        return 0.0

    return -np.inf

# ============================================================
# Likelihood
# ============================================================

def log_likelihood(theta):

    model = transit_model(theta)

    chi2 = np.sum(
        ((flux-model)/flux_err)**2
    )

    return -0.5*chi2

# ============================================================
# Posterior
# ============================================================

def log_probability(theta):

    lp = log_prior(theta)

    if not np.isfinite(lp):
        return -np.inf

    return lp + log_likelihood(theta)

# ============================================================
# Initial Guess
# Literature values
# ============================================================

initial = np.array([

    0.13,
    5.6,
    89.3

])

# ============================================================
# Initialize walkers
# ============================================================

nwalkers = 32

ndim = 3

pos = initial + 1e-4*np.random.randn(
    nwalkers,
    ndim
)

# ============================================================
# Run MCMC
# ============================================================

sampler = emcee.EnsembleSampler(

    nwalkers,
    ndim,
    log_probability

)

print("Running MCMC...")

sampler.run_mcmc(

    pos,

    5000,

    progress=True

)

print("Finished!")

# ============================================================
# Remove Burn-in
# ============================================================

samples = sampler.get_chain(

    discard=1000,

    thin=10,

    flat=True

)

# ============================================================
# Best-fit Parameters
# ============================================================

rp_fit = np.median(samples[:,0])
a_fit = np.median(samples[:,1])
inc_fit = np.median(samples[:,2])

print("====================================")

print("Best-fit Parameters")

print("====================================")

print("Rp/R* =",rp_fit)
print("a/R*  =",a_fit)
print("inc   =",inc_fit)

# ============================================================
# Plot Best-fit Model
# ============================================================

best_model = transit_model(

    [rp_fit,a_fit,inc_fit]

)

plt.figure(figsize=(10,5))

plt.scatter(

    phase,

    flux,

    s=18,

    color="gray",

    alpha=0.6,

    label="Observation"

)

plt.plot(

    phase,

    best_model,

    color="red",

    lw=3,

    label="Best-fit Batman"

)

plt.xlabel("Phase (days)",fontsize=14)

plt.ylabel("Normalized Flux",fontsize=14)

plt.title("Figure 7. Best-fit Transit Model",fontsize=18)

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

# ============================================================
# Trace Plot
# ============================================================

chain = sampler.get_chain()

labels = [

    "Rp/R*",

    "a/R*",

    "inc"

]

fig,axes = plt.subplots(

    3,

    figsize=(10,8),

    sharex=True

)

for i in range(3):

    axes[i].plot(

        chain[:,:,i],

        alpha=0.3

    )

    axes[i].set_ylabel(labels[i])

axes[-1].set_xlabel("Step")

plt.tight_layout()

plt.show()

# ============================================================
# Corner Plot
# ============================================================

corner.corner(

    samples,

    labels=labels,

    truths=[

        rp_fit,

        a_fit,

        inc_fit

    ],

    show_titles=True

)

plt.show()


# In[5]:


# ============================================================
# Kepler-17b Transit Fitting with Batman + emcee
# Step 1 : Read data & Build Transit Model
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import batman
import emcee
import corner

# ============================================================
# Read phase-folded data (ALL points)
# ============================================================

phase_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_folded_normalized.csv"

phase_df = pd.read_csv(phase_file)

phase = phase_df["phase"].values
flux = phase_df["flux"].values

print("Phase-folded data loaded.")
print("Number of points:", len(phase))

# ============================================================
# Read binned data (for plotting only)
# ============================================================

bin_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_binned_normalized.csv"

bin_df = pd.read_csv(bin_file)

phase_bin = bin_df["phase"].values
flux_bin = bin_df["flux"].values

print("Binned data loaded.")
print("Number of bins:", len(phase_bin))

# ============================================================
# Convert phase to real time
# ============================================================

INITIAL_PERIOD = 1.4857108

phase_time = phase * INITIAL_PERIOD
phase_time_bin = phase_bin * INITIAL_PERIOD

print()
print("Time conversion")
print("------------------------------")
print("Phase range: [{:.3f}, {:.3f}]".format(phase.min(), phase.max()))
print("Time range: [{:.3f}, {:.3f}] days".format(phase_time.min(), phase_time.max()))

# ============================================================
# Fixed Parameters (from literature)
# ============================================================

FIXED_U1 = 0.47
FIXED_U2 = 0.14
FIXED_OFFSET = 1.0
FIXED_PERIOD = 1.4857108

print()
print("Fixed Parameters")
print("------------------------------")
print("u1     =", FIXED_U1)
print("u2     =", FIXED_U2)
print("offset =", FIXED_OFFSET)
print("period =", FIXED_PERIOD)

# ============================================================
# Batman Transit Model
# ============================================================

def transit_model(theta, time):

    """
    theta = [Rp/R*, a/R*, inc, t0]
    """

    rp, a, inc, t0 = theta

    params = batman.TransitParams()

    params.t0 = t0

    params.per = FIXED_PERIOD

    params.rp = rp

    params.a = a

    params.inc = inc

    params.ecc = 0.0

    params.w = 90.0

    params.u = [FIXED_U1, FIXED_U2]

    params.limb_dark = "quadratic"

    m = batman.TransitModel(params, time)

    model = m.light_curve(params)

    return model

# ============================================================
# Prior
# ============================================================

def log_prior(theta):

    rp, a, inc, t0 = theta

    if not (0.08 < rp < 0.18):
        return -np.inf

    if not (4.0 < a < 7.0):
        return -np.inf

    if not (87.0 < inc < 90.0):
        return -np.inf

    if not (-0.05 < t0 < 0.05):
        return -np.inf

    return 0.0

# ============================================================
# Likelihood
# ============================================================

transit_mask = np.abs(phase) < 0.02
out_of_transit_flux = flux[~transit_mask]
sigma = np.std(out_of_transit_flux - np.median(out_of_transit_flux))

print()
print("Estimated sigma (out-of-transit only) =", sigma)

def log_likelihood(theta):

    model = transit_model(theta, phase_time)

    chi2 = np.sum(((flux - model) / sigma) ** 2)

    return -0.5 * chi2

# ============================================================
# Posterior
# ============================================================

def log_probability(theta):

    lp = log_prior(theta)

    if not np.isfinite(lp):

        return -np.inf

    return lp + log_likelihood(theta)

# ============================================================
# Initial Guess
# ============================================================

initial = np.array([
    0.13,       # Rp/R* (literature ~0.13)
    5.7,        # a/R* (literature ~5.7)
    89.0,       # inclination (literature ~89.0)
    0.0         # t0
])

print()
print("Initial Guess")
print("----------------------")
print("Rp/R* =", initial[0])
print("a/R*  =", initial[1])
print("inc   =", initial[2])
print("t0    =", initial[3])

# ============================================================
# emcee Settings
# ============================================================

ndim = len(initial)

nwalkers = 64

pos = initial + [0.01, 0.5, 0.5, 0.01] * np.random.randn(nwalkers, ndim)

print()
print("==============================")
print("MCMC Ready")
print("==============================")
print("Dimensions :", ndim)
print("Walkers    :", nwalkers)
print("Total free parameters:")
print("Rp/R*")
print("a/R*")
print("inc")
print("t0")
print("==============================")

# ============================================================
# Run MCMC
# ============================================================

print()
print("===================================")
print("Running MCMC...")
print("===================================")

sampler = emcee.EnsembleSampler(
    nwalkers,
    ndim,
    log_probability
)

sampler.run_mcmc(
    pos,
    6000,
    progress=True
)

print()
print("===================================")
print("MCMC Finished!")
print("===================================")

# ============================================================
# Remove Burn-in
# ============================================================

burnin = 2000

thin = 10

samples = sampler.get_chain(
    discard=burnin,
    thin=thin,
    flat=True
)

print()
print("Posterior Samples:", len(samples))

# ============================================================
# Acceptance Fraction
# ============================================================

acc = np.mean(sampler.acceptance_fraction)

print()
print("Mean Acceptance Fraction = {:.4f}".format(acc))

if 0.2 < acc < 0.5:
    print("Sampling looks good.")
else:
    print("Warning: acceptance fraction may be abnormal.")

# ============================================================
# Parameter Estimation
# ============================================================

labels = [
    "Rp/R*",
    "a/R*",
    "inc",
    "t0"
]

print()
print("===================================")
print("Best-fit Parameters")
print("===================================")

best_theta = []

for i, label in enumerate(labels):

    q16, q50, q84 = np.percentile(
        samples[:, i],
        [16, 50, 84]
    )

    lower = q50 - q16
    upper = q84 - q50

    best_theta.append(q50)

    print(
        f"{label:8s} = "
        f"{q50:.6f} "
        f"+{upper:.6f} "
        f"-{lower:.6f}"
    )

best_theta = np.array(best_theta)

# ============================================================
# Walker Trace
# ============================================================

chain = sampler.get_chain()

fig, axes = plt.subplots(
    ndim,
    figsize=(10, 10),
    sharex=True
)

for i in range(ndim):

    ax = axes[i]

    ax.plot(
        chain[:, :, i],
        alpha=0.3,
        lw=0.5
    )

    ax.set_ylabel(labels[i])

axes[-1].set_xlabel("Step")

plt.tight_layout()

plt.show()

# ============================================================
# Corner Plot
# ============================================================

corner.corner(

    samples,

    labels=labels,

    truths=best_theta,

    quantiles=[0.16, 0.5, 0.84],

    show_titles=True,

    title_fmt=".6f",

    title_kwargs={"fontsize": 11},

    label_kwargs={"fontsize": 12},

    fill_contours=True,

    plot_density=True,

    smooth=1.0,

    smooth1d=1.0,

    levels=(0.393, 0.865, 0.989)
)

plt.show()

# ============================================================
# Best-fit Transit Model
# ============================================================

model = transit_model(
    best_theta,
    phase_time
)

model_bin = transit_model(
    best_theta,
    phase_time_bin
)

# ============================================================
# Best-fit Figure
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    phase,
    flux,
    s=3,
    color="lightgray",
    alpha=0.5,
    label="Phase-folded data"
)

plt.scatter(
    phase_bin,
    flux_bin,
    s=28,
    color="black",
    label="Binned data"
)

plt.plot(
    phase_bin,
    model_bin,
    color="red",
    lw=2.5,
    label="Best-fit Batman model"
)

plt.xlabel("Orbital Phase", fontsize=13)
plt.ylabel("Normalized Flux", fontsize=13)

plt.title("Kepler-17b Transit Fit", fontsize=15)

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

# ============================================================
# Residual Plot
# ============================================================

residual = flux - model

plt.figure(figsize=(10, 3))

plt.scatter(
    phase,
    residual,
    s=3,
    color="black"
)

plt.axhline(
    0,
    color="red",
    ls="--"
)

plt.xlabel("Orbital Phase")

plt.ylabel("Residual")

plt.title("Fit Residuals")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# In[1]:


# ============================================================
# Kepler-17b Transit Fitting with Batman + emcee
# Full 8-Parameter Fitting with Gaussian Priors
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import batman
import emcee
import corner

# ============================================================
# Read phase-folded data (ALL points)
# ============================================================

phase_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_folded_normalized.csv"

phase_df = pd.read_csv(phase_file)

phase = phase_df["phase"].values
flux = phase_df["flux"].values

print("Phase-folded data loaded.")
print("Number of points:", len(phase))

# ============================================================
# Read binned data (for plotting only)
# ============================================================

bin_file = r"C:\Users\21665\Desktop\kepler17\Kepler17_phase_binned_normalized.csv"

bin_df = pd.read_csv(bin_file)

phase_bin = bin_df["phase"].values
flux_bin = bin_df["flux"].values

print("Binned data loaded.")
print("Number of bins:", len(phase_bin))

# ============================================================
# Gaussian Prior Parameters (from literature)
# ============================================================

U1_LIT = 0.47
U1_SIGMA = 0.05
U2_LIT = 0.14
U2_SIGMA = 0.05
PERIOD_LIT = 1.4857108
PERIOD_SIGMA = 0.001

print()
print("Gaussian Priors")
print("------------------------------")
print("u1      ~ N({:.6f}, {:.4f})".format(U1_LIT, U1_SIGMA))
print("u2      ~ N({:.6f}, {:.4f})".format(U2_LIT, U2_SIGMA))
print("period  ~ N({:.7f}, {:.6f})".format(PERIOD_LIT, PERIOD_SIGMA))

# ============================================================
# Batman Transit Model
# ============================================================

def transit_model(theta, time):
    """
    theta = [Rp/R*, a/R*, inc, t0, u1, u2, offset, period]
    """
    rp, a, inc, t0, u1, u2, offset, period = theta

    params = batman.TransitParams()
    params.t0 = t0
    params.per = period
    params.rp = rp
    params.a = a
    params.inc = inc
    params.ecc = 0.0
    params.w = 90.0
    params.u = [u1, u2]
    params.limb_dark = "quadratic"

    m = batman.TransitModel(params, time)
    model = m.light_curve(params)

    return model * offset

# ============================================================
# Prior (uniform + Gaussian)
# ============================================================

def log_prior(theta):
    rp, a, inc, t0, u1, u2, offset, period = theta

    # Hard uniform priors
    if not (0.08 < rp < 0.18):
        return -np.inf
    if not (4.0 < a < 7.0):
        return -np.inf
    if not (87.0 < inc < 90.0):
        return -np.inf
    if not (-0.05 < t0 < 0.05):
        return -np.inf
    if not (0.0 < u1 < 1.0):
        return -np.inf
    if not (0.0 < u2 < 1.0):
        return -np.inf
    if not (0.95 < offset < 1.05):
        return -np.inf
    if not (1.48 < period < 1.49):
        return -np.inf

    # Gaussian priors (soft constraints)
    lp_u1 = -0.5 * ((u1 - U1_LIT) / U1_SIGMA) ** 2
    lp_u2 = -0.5 * ((u2 - U2_LIT) / U2_SIGMA) ** 2
    lp_period = -0.5 * ((period - PERIOD_LIT) / PERIOD_SIGMA) ** 2

    return lp_u1 + lp_u2 + lp_period

# ============================================================
# Likelihood
# ============================================================

transit_mask = np.abs(phase) < 0.02
out_of_transit_flux = flux[~transit_mask]
sigma = np.std(out_of_transit_flux - np.median(out_of_transit_flux))

print()
print("Estimated sigma (out-of-transit only) =", sigma)

def log_likelihood(theta):
    rp, a, inc, t0, u1, u2, offset, period = theta
    phase_time = phase * period
    model = transit_model(theta, phase_time)
    chi2 = np.sum(((flux - model) / sigma) ** 2)
    return -0.5 * chi2

# ============================================================
# Posterior
# ============================================================

def log_probability(theta):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta)

# ============================================================
# Initial Guess
# ============================================================

initial = np.array([
    0.13,           # Rp/R*
    5.7,            # a/R*
    89.0,           # inc
    0.0,            # t0
    0.47,           # u1
    0.14,           # u2
    1.0,            # offset
    1.4857108       # period
])

print()
print("Initial Guess")
print("----------------------")
print("Rp/R*  =", initial[0])
print("a/R*   =", initial[1])
print("inc    =", initial[2])
print("t0     =", initial[3])
print("u1     =", initial[4])
print("u2     =", initial[5])
print("offset =", initial[6])
print("period =", initial[7])

# ============================================================
# emcee Settings
# ============================================================

ndim = len(initial)
nwalkers = 128

pos = initial + [
    0.01,    # Rp/R*
    0.3,     # a/R*
    0.3,     # inc
    0.01,    # t0
    0.05,    # u1
    0.05,    # u2
    0.01,    # offset
    0.001    # period
] * np.random.randn(nwalkers, ndim)

print()
print("==============================")
print("MCMC Ready")
print("==============================")
print("Dimensions :", ndim)
print("Walkers    :", nwalkers)
print("Total free parameters:")
print("Rp/R*, a/R*, inc, t0, u1, u2, offset, period")
print("==============================")

# ============================================================
# Run MCMC
# ============================================================

print()
print("===================================")
print("Running MCMC...")
print("===================================")

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability)
sampler.run_mcmc(pos, 10000, progress=True)

print()
print("===================================")
print("MCMC Finished!")
print("===================================")

# ============================================================
# Remove Burn-in
# ============================================================

burnin = 4000
thin = 10

samples = sampler.get_chain(discard=burnin, thin=thin, flat=True)

print()
print("Posterior Samples:", len(samples))

# ============================================================
# Acceptance Fraction
# ============================================================

acc = np.mean(sampler.acceptance_fraction)

print()
print("Mean Acceptance Fraction = {:.4f}".format(acc))

if 0.2 < acc < 0.5:
    print("Sampling looks good.")
else:
    print("Warning: acceptance fraction may be abnormal.")

# ============================================================
# Parameter Estimation
# ============================================================

labels = ["Rp/R*", "a/R*", "inc", "t0", "u1", "u2", "offset", "period"]

print()
print("===================================")
print("Best-fit Parameters")
print("===================================")

best_theta = []

for i, label in enumerate(labels):
    q16, q50, q84 = np.percentile(samples[:, i], [16, 50, 84])
    lower = q50 - q16
    upper = q84 - q50
    best_theta.append(q50)

    print(f"{label:8s} = {q50:.6f} +{upper:.6f} -{lower:.6f}")

best_theta = np.array(best_theta)

# ============================================================
# Calculate impact parameter b = (a/R*) * cos(inc)
# ============================================================

a_vals = samples[:, 1]
inc_vals = samples[:, 2]
b_vals = a_vals * np.cos(np.deg2rad(inc_vals))

b_q16, b_q50, b_q84 = np.percentile(b_vals, [16, 50, 84])
print()
print("Derived impact parameter:")
print("b = {:.6f} +{:.6f} -{:.6f}".format(b_q50, b_q84 - b_q50, b_q50 - b_q16))

# ============================================================
# Walker Trace
# ============================================================

chain = sampler.get_chain()

fig, axes = plt.subplots(ndim, figsize=(10, 14), sharex=True)

for i in range(ndim):
    ax = axes[i]
    ax.plot(chain[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(chain))
    ax.set_ylabel(labels[i])
    ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel("Step number")

plt.tight_layout()
plt.savefig("MCMC_full_trace.png", dpi=150)
plt.close()

print()
print("Walker trace saved: MCMC_full_trace.png")

# ============================================================
# Corner Plot
# ============================================================

fig = corner.corner(
    samples,
    labels=labels,
    quantiles=[0.16, 0.5, 0.84],
    show_titles=True,
    title_kwargs={"fontsize": 9},
    truths=initial,
    truth_color="red",
    plot_datapoints=True,
    plot_density=True,
    fill_contours=True,
    smooth=0.9,
    levels=[0.68, 0.95],
    figsize=(12, 12)
)

plt.savefig("MCMC_full_corner.png", dpi=150)
plt.close()

print()
print("Corner plot saved: MCMC_full_corner.png")

# ============================================================
# Plot Best-fit Model
# ============================================================

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(phase_bin, flux_bin, "k.", markersize=5, label="Binned data")

phase_model = np.linspace(-0.5, 0.5, 500)
time_model = phase_model * best_theta[7]
model_flux = transit_model(best_theta, time_model)

ax.plot(phase_model, model_flux, "r-", linewidth=2, label="Best-fit model")

ax.set_xlabel("Phase")
ax.set_ylabel("Normalized Flux")
ax.set_title("Kepler-17b Transit - Full 8-Parameter Fit")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("MCMC_full_fit.png", dpi=150)
plt.close()

print()
print("Best-fit plot saved: MCMC_full_fit.png")

# ============================================================
# Save Results
# ============================================================

results_df = pd.DataFrame({
    "Parameter": labels + ["b"],
    "Best_fit": list(best_theta) + [b_q50],
    "Lower_error": [np.percentile(samples[:, i], 16) for i in range(ndim)] + [b_q16],
    "Upper_error": [np.percentile(samples[:, i], 84) for i in range(ndim)] + [b_q84]
})

results_df.to_csv("MCMC_full_results.csv", index=False)

print()
print("Results saved: MCMC_full_results.csv")

print()
print("=" * 50)
print("MCMC Full 8-Parameter Fitting Complete!")
print("=" * 50)


# In[ ]:




