# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:01:51 2020

@author: Ahmed
"""
import pandas
import numpy as np

def xmtrLoader(pathname, filename="/data/xmtr.lis"):
    df = pandas.read_table(pathname+filename, skiprows=1, 
                           delim_whitespace=True, names=('xmtr_id','freq', 'lat','lon', 'pwr','incl', 'headng', 'alt', 'location'))
    endIdx = df[df["xmtr_id"]== "end"].index
    df.drop(endIdx, inplace=True)
    return df
def areaLoader(pathname, filename="/data/area.lis"):
    df = pandas.read_table(pathname+filename, skiprows=1, 
                           delim_whitespace=True, names=('area_id', 'lat1', 'lon1', 'lat2','lon2'))
    endIdx = df[df["area_id"]== "end"].index
    df.drop(endIdx, inplace=True)
    return df
def rxLoader(pathname, filename = "/data/rx.lis"):
    try:
        df = pandas.read_table(pathname+filename, skiprows=1, 
                           delim_whitespace=True, names=('rx_id', 'lat','lon'))
    except:
        with open(pathname+filename, "w+") as f:
            f.write("rx_id    lat    lon\n")
            f.writelines("Tunisia \t 36.8 \t -10.22\n")
            f.writelines("Algeria \t 36.76 \t -3.47\n")
            f.close()
        
    finally:
        df = pandas.read_table(pathname+filename, skiprows=1, 
                           delim_whitespace=True, names=('rx_id', 'lat','lon'))

    return df

def gcpathLoader(pathname, filename="/gcpath.log"):
    df_gcpath = pandas.read_table(pathname+filename, skiprows=14, delim_whitespace=True,
                                  names=('xmtr_id', 'tlat', 'tlon', 'bearing', 'range',
                                         'rlat', 'rlon', 'rrho'))
    df_gcpathAmb = pandas.read_table(pathname+filename, skiprows=16, delim_whitespace=True,
                                  names=('rho', 'lat', 'lon', 'azim', 'dip', 'bfield', 'sigma',
                                         'epsr', 'ncd', 'chi', 'beta', 'hprime', 'npr'))
    
    endIdx = df_gcpathAmb[df_gcpathAmb['rho']== 'quit'].index
    df_gcpathAmb.drop(endIdx, inplace=True)
    df_gcpathAmb.drop(endIdx+1, inplace=True)
    return df_gcpath[0:1], df_gcpathAmb

def bearingsLoader(pathname, filename="/bearings.log"):
    """
    Load bearings data from bearings.log
    """
    df_bearings_path_info = pandas.read_table(pathname+filename, skiprows=21, delim_whitespace=True,
                                  names=("nr", "rho", "lat", "lon", "azim",
                                         "dip", "sigma", "chi", "beta", "h'"))
    endIdx = df_bearings_path_info[df_bearings_path_info["nr"]== 'PRFL_HGTS:'].index
    #print(endIdx)
    df_bearings_path_info = df_bearings_path_info[0:endIdx[0]]
    # Find signal prop: dist, Amp, Phase
    with open(pathname+filename) as f:
        content = f.readlines()
    # Pointeur = 'z component'
    index = [x for x in range(len(content)) if 'z component' in content[x].lower()]
    indexrows =index[0] + 2
    
    df_bearings_ambient = pandas.read_table(pathname+filename, skiprows= indexrows, delim_whitespace=True,
                                  names=("dist1", "amplitude1", "phase1", "dist2", "amplitude2", "phase2",
                                         "dist3", "amplitude3", "phase3"))
    endIdx = df_bearings_ambient[df_bearings_ambient["dist1"]== 'nc'].index
    df_bearings_ambient = df_bearings_ambient[0:endIdx[0]].dropna()
    df1 = df_bearings_ambient[["dist1", "amplitude1", "phase1"]]
    df2 = df_bearings_ambient[["dist2", "amplitude2", "phase2"]]
    df3 = df_bearings_ambient[["dist3", "amplitude3", "phase3"]]
    df_ambient = np.vstack((np.array(df1, dtype = np.float64),
                            np.array(df2, dtype = np.float64),
                            np.array(df3, dtype = np.float64)))
    return df_bearings_path_info , df_ambient
def rexpLoader(pathname, filename="/rexp.log"):
    """
    Load rexp data from rexp.log
    """
#    df_rexp_path_info = pandas.read_table(pathname+filename, skiprows=23, delim_whitespace=True,
#                                  names=("nr", "rho", "lat", "lon", "azim",
#                                         "dip", "sigma", "chi", "beta", "h'"))
#    endIdx = df_rexp_path_info[df_rexp_path_info["nr"]== 'PRFL_HGTS:'].index
#    df_rexp_path_info = df_rexp_path_info[0:endIdx[0]]
    # Find signal prop: dist, Amp, Phase
    with open(pathname+filename) as f:
        content = f.readlines()
    # Pointeur = 'z component'
    index = [x for x in range(len(content)) if 'z component' in content[x].lower()]
    indexrows =index[0] + 2
    
    df_rexp_disturb = pandas.read_table(pathname+filename, skiprows= indexrows, delim_whitespace=True,
                                  names=("dist1", "amplitude1", "phase1", "dist2", "amplitude2", "phase2",
                                         "dist3", "amplitude3", "phase3"))
    endIdx = df_rexp_disturb[df_rexp_disturb["dist1"]== 'nc'].index
    df_rexp_disturb = df_rexp_disturb[0:endIdx[0]].dropna()
    df1 = df_rexp_disturb[["dist1", "amplitude1", "phase1"]]
    df2 = df_rexp_disturb[["dist2", "amplitude2", "phase2"]]
    df3 = df_rexp_disturb[["dist3", "amplitude3", "phase3"]]
    df_disturb = np.vstack((np.array(df1, dtype = np.float64),
                            np.array(df2, dtype = np.float64),
                            np.array(df3, dtype = np.float64)))
    return df_disturb


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from scipy import interpolate
    df_gcpath, df_gcpathAmb = gcpathLoader(pathname= "../lwpcv21")
    bearing, range_max = df_gcpath["bearing"], df_gcpath["rrho"]
    print("bearing = ", float(bearing), "range max = ", float(range_max))
    print("beta amb = ", df_gcpathAmb['beta'][0])
    print("hprime amb = ", df_gcpathAmb['hprime'][0])
    ## FIGURE
    rho = df_gcpathAmb['rho']
    rho = np.array(rho, dtype = np.float64)
    hprime = df_gcpathAmb['hprime']
    hprime =np.array(hprime, dtype = np.float64)
    beta = df_gcpathAmb['beta']
    beta =np.array(beta, dtype = np.float64)
    f = interpolate.interp1d(rho, hprime)
    g = interpolate.interp1d(rho, beta)
    newrho = np.arange(0, max(rho), 20)
    newhprime = f(newrho)
    newbeta = g(newrho)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(8,5))
    ax1.plot(rho/1000, hprime, "ro")
    ax1.plot(newrho/1000, newhprime, "-r")
    ax1.set_title("H' new stratified maillor")
    ax1.set_xlabel("rho (Mm)")
    ax1.set_ylabel("h' (km)")
    ax2.plot(rho/1000, beta, "ro")
    ax2.plot(newrho/1000, newbeta, "r-")
    ax2.set_title("Beta new stratified maillor")
    ax2.set_xlabel("rho (Mm)")
    ax2.set_ylabel("Beta' (km^-1)")
    
    
    # perturbation grid
    hmodel = np.ones(len(newhprime))
    for k in np.arange(0,10,10/10):
        for i in range(len(newhprime)):
            if 72<= newhprime[i] <= 76:
                hmodel[i]= newhprime[i]-k
            else:
                hmodel[i]= newhprime[i]
        ax1.plot(newrho/1000, hmodel, "bo-", ms=2, alpha = 0.5)
        
    betamodel = np.ones(len(newbeta))
    for k in np.arange(0,0.2,0.2/10):
        for i in range(len(newbeta)):
            if 0.29 <= newbeta[i] <= 0.32:
                betamodel[i]= newbeta[i]-k
            else:
                betamodel[i]= newbeta[i]
        ax2.plot(newrho/1000, betamodel, "bo-",ms=2, alpha = 0.5)
    
    plt.tight_layout()
    df_bearings_path_info , df_ambient = bearingsLoader(pathname= "../lwpcv21")
    df_disturb = rexpLoader(pathname= "../lwpcv21")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(8,5))
    ax1.plot(df_ambient[:,0], df_ambient[:,1], "b-")
    ax1.plot(df_disturb[:-1,0], df_disturb[:-1,1], "r-")
    ax1.set_ylabel("Amplitude")
    ax2.plot(df_ambient[:,0], df_ambient[:,2], "b-")
    ax2.plot(df_disturb[:-1,0], df_disturb[:-1,2], "r-")
    ax2.set_xlabel("rho [km]")
    ax2.set_ylabel("Phase")
    plt.suptitle("Hello!", fontsize = 14, color = "r", fontweight = "bold")
    plt.show()
    


