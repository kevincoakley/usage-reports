%s

var data = [ %s ];

var layout = {
    title:'%s',
    barmode: 'group',
    showlegend: true,
    "xaxis": {
        "title": "%s"
    },
    "yaxis": {
        "title": "%s"
    },
};

Plotly.newPlot('myDiv', data, layout);
