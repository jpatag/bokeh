'''
A 2-D coordinate plot that demonstrates custom tooltips and notes
attached to various dots on the graph. This example demonstrates
how customizable points are on graphs.

.. bokeh-example-metadata::
    :apis: bokeh.models.ColumnDataSource, bokeh.plotting.figure, bokeh.plotting.show
    :keywords: custom, tooltip, hover, point, plot
'''

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    desc=['A', 'b', 'C', 'd', 'E'],
    imgs=[
        'https://docs.bokeh.org/static/snake.jpg',
        'https://docs.bokeh.org/static/snake2.png',
        'https://docs.bokeh.org/static/snake3D.png',
        'https://docs.bokeh.org/static/snake4_TheRevenge.png',
        'https://docs.bokeh.org/static/snakebite.jpg',
    ],
    fonts=[
        '<i>italics</i>',
        '<pre>pre</pre>',
        '<b>bold</b>',
        '<small>small</small>',
        '<del>del</del>',
    ],
))

TOOLTIPS = """
    <div>
        <div>
            <img
                src="@imgs" height="42" alt="@imgs" width="42"
                style="float: left; margin: 0px 15px 15px 0px;"
                border="2"
            ></img>
        </div>
        <div>
            <span style="font-size: 17px; font-weight: bold;">@desc</span>
            <span style="font-size: 15px; color: #966;">[$index]</span>
        </div>
        <div>
            <span>@fonts{safe}</span>
        </div>
        <div>
            <span style="font-size: 15px;">Location</span>
            <span style="font-size: 10px; color: #696;">($x, $y)</span>
        </div>
    </div>
"""

p = figure(width=400, height=400, tooltips=TOOLTIPS,
           title="Mouse over the dots")

p.scatter('x', 'y', size=20, source=source)

show(p)
