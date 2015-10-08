var team2 = {
    x: ['2015-10-01', '2015-10-02', '2015-10-03'],
    y: [5.00, 0.50, 2.25],
    name: 'team2',
    type: 'bar'
};



var data = [ team2 ];

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
