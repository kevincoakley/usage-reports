var team1 = {
    x: ['2015-10-01', '2015-10-02', '2015-10-03'],
    y: [3.33, 0.50, 1.75],
    name: 'team1',
    type: 'bar'
};



var data = [ team1 ];

var layout = {
    title:'AWS Tag Cost (delayed by 12 hours)',
    barmode: 'group',
    showlegend: true,
    "xaxis": {
        "title": "Date (UTC)"
    },
    "yaxis": {
        "title": "Cost"
    },
};

Plotly.newPlot('myDiv', data, layout);
