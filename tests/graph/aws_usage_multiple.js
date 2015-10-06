var team1 = {
    x: ['2015-10-01', '2015-10-02', '2015-10-03'],
    y: [3.33, 0.50, 1.75],
    name: 'team1',
    type: 'bar'
};

var team2 = {
    x: ['2015-10-01', '2015-10-02', '2015-10-03'],
    y: [5.00, 0.50, 2.25],
    name: 'team2',
    type: 'bar'
};

var team3 = {
    x: ['2015-10-01', '2015-10-02', '2015-10-03'],
    y: [0.25, 1.50, 4.25],
    name: 'team3',
    type: 'bar'
};



var data = [ team1, team2, team3 ];

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
