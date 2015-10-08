var team3 = {
    x: ['2015-10-01', '2015-10-02', '2015-10-03'],
    y: [0.25, 1.50, 4.25],
    name: 'team3',
    type: 'bar'
};



var data = [ team3 ];

var layout = {
    title:'AWS Cluster Cost',
    barmode: 'group',
    showlegend: true,
    "xaxis": {
        "title": "Date"
    },
    "yaxis": {
        "title": "Cost"
    },
};

Plotly.newPlot('myDiv', data, layout);
