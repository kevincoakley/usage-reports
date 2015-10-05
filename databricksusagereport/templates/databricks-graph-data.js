%s

var data = [ %s ];

var layout = {
    title:'%s',
    barmode: 'group',
    showlegend: true,
    "xaxis": {
        "title": "Date & Hour"
    },
    "yaxis": {
        "title": "Workers"
    },
};

Plotly.newPlot('myDiv', data, layout);
