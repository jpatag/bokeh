'''
A basic freehand drawing tool. This example demonstraets different ways
to implement tools in Bokeh. In this context, this tool allows the user
to freehand draw on a plot and save the resulting plot as a PNG file.

.. bokeh-examples-metadata::
    :apis: bokeh.models, bokeh.plotting.figure.line, bokeh.plotting.show
    :keywords: draw, freehand, tool
'''

from bokeh.models import FreehandDrawTool
from bokeh.plotting import figure, show

p = figure(x_range=(0, 10), y_range=(0, 10), width=400, height=400,
           title='Freehand Draw Tool')

r = p.multi_line([[1, 9]], [[5, 5]], line_width=5, alpha=0.4, color='red')

draw_tool = FreehandDrawTool(renderers=[r], num_objects=3)
p.add_tools(draw_tool)
p.toolbar.active_drag = draw_tool

show(p)
