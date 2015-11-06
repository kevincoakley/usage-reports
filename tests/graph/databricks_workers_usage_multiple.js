var team1 = {
    x: ['2015-10-01 01', '2015-10-01 02', '2015-10-01 03', '2015-10-01 04'],
    y: [4, 4, 4, 6],
    name: 'team1',
    type: 'bar'
};

var team2 = {
    x: ['2015-10-01 01', '2015-10-01 02', '2015-10-01 03', '2015-10-01 04'],
    y: [8, 6, 10, 8],
    name: 'team2',
    type: 'bar'
};

var team3 = {
    x: ['2015-10-01 01', '2015-10-01 02', '2015-10-01 03', '2015-10-01 04'],
    y: [6, 8, 6, 8],
    name: 'team3',
    type: 'bar'
};



var data = [ team1, team2, team3 ];

var layout = {
    title:'Cluster Worker Usage',
    barmode: 'group',
    showlegend: true,
    "xaxis": {
        "title": "Date & Hour (Pacific Time Zone)"
    },
    "yaxis": {
        "title": "Workers"
    },
};

Plotly.newPlot('myDiv', data, layout);
