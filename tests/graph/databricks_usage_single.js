var team1 = {
    x: ['2015-10-01 01'],
    y: [4],
    name: 'team1',
    type: 'bar'
};

var team2 = {
    x: ['2015-10-01 01'],
    y: [8],
    name: 'team2',
    type: 'bar'
};

var team3 = {
    x: ['2015-10-01 01'],
    y: [6],
    name: 'team3',
    type: 'bar'
};



var data = [ team1, team2, team3 ];

var layout = {
    title:'Cluster Worker Usage',
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
