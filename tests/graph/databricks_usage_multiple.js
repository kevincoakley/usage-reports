var team1 = {
    x: ['2015-10-01 01:00:00', '2015-10-01 02:00:00', '2015-10-01 03:00:00', '2015-10-01 04:00:00'],
    y: [4, 4, 4, 6],
    name: 'team1',
    mode: 'lines+markers'
};

var team2 = {
    x: ['2015-10-01 01:00:00', '2015-10-01 02:00:00', '2015-10-01 03:00:00', '2015-10-01 04:00:00'],
    y: [8, 6, 10, 8],
    name: 'team2',
    mode: 'lines+markers'
};

var team3 = {
    x: ['2015-10-01 01:00:00', '2015-10-01 02:00:00', '2015-10-01 03:00:00', '2015-10-01 04:00:00'],
    y: [6, 8, 6, 8],
    name: 'team3',
    mode: 'lines+markers'
};



var data = [ team1, team2, team3 ];

var layout = {
    title:'Cluster Worker Usage',
    autosize: true,
};

Plotly.newPlot('myDiv', data, layout);
