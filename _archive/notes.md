config notebook -> use concrete env


# Pin versions for mpl-interactions
mpl-interactions -> the tutorial uses 0.22.0
ipywidgets=8.1.1  -> the tutorial uses 7.7.0
ipympl   0.9.3 # compatible with matplotlib>=3.4.0, have matplotlib=3.6.2 -> the tutorial uses 0.9.1


https://github.com/matplotlib/ipympl/issues/460
https://github.com/matplotlib/ipympl/issues/460#issuecomment-1100202141
This looks like the the widgets version 8 manager. Currentl ipympl requires ipywidgets< 8 but somehow that's not getting cleared. If you can get the javascript of ipywidgets back to pre version 8 it should fixes things. But that's just a workaround, we really need to just update our requirements (which will require testing for the new ipywidgets

I also had to install the latest version of nodejs (mamba install nodejs)


# Widgets overview
https://minrk-ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Numeric-widgets

# 
dash: only possible to have one slider
bokeh: two sliders may be possibe
(1) x is a str or time data
läuft die grafik einigermaßen schnell?
x axis muss year month sein

