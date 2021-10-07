# -*- coding: utf-8 -*-


def DiscretisedColormap(CmapName_str, Ncolors_int=11, will_print=True):
    """
    ========================================== Parameters ==========================================
    - CmapName_str : string. The name of the python colormap ('viridis', 'plasma', 'twilight', ...)
    - Ncolors_int : integer. The number of colors to extract from the colormap, 11 by default.
    - will_print : bool. The way the function give its result. True by default.

    ============================================ Returns ===========================================
    A string that is composed of the RGB triplets and hexadecimal codes for each color extracted
    from the colormap described by CmapName_str. Ncolors_int triplets and hexcodes will compose this
    string. The string is by default printed in the console, and can this way be copy pasted in any
    desired file. If will_print=False, the function only retuns the whole string and it can be used
    in file.write(DiscretisedColormap('viridis', 11, False)) file being a .gpl, for example.
    """
    # ============================== Importations and initialisations ==============================
    from matplotlib import cm
    from matplotlib.colors import rgb2hex

    cmap = cm.get_cmap(CmapName_str)
    all_cols_str = ""
    # ======================================= Discretisation =======================================
    for n in range(Ncolors_int):  # Looping through the number of colors to extract from colormap
        idx = int(round(n*(cmap.N-1)/(Ncolors_int-1)))  # Index of the color to extract
        col_RGB = cmap(idx)[:-1]  # RGB code of the concerned color
        hex_code = rgb2hex(col_RGB).upper()  # And its hexadecimal code
        # ============================== Creation of the clean string ==============================
        clean_col_str = ""
        for X in col_RGB:  # For each element of the RGB triplet
            # Conversion in [0:255] range, rounding, conversion to integer and then to string :
            X_str = str(int(round(X*255)))
            # Spaces addition to have a string length = 3 for either R, G or B value :
            clean_X = ' '*(3-len(X_str))+X_str
            clean_col_str = clean_col_str+clean_X+' '  # Concatenation and spacing between values
        # Addition of the hexadecimal code and expansion of the big color list :
        all_cols_str = all_cols_str+clean_col_str+hex_code+'\n'
    # =========================================== Result ===========================================
    if will_print is True:
        print(all_cols_str)
    else:
        return all_cols_str
