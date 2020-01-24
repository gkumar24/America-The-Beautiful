var p1 = d3.json('static/json/natparks_geo.json');
var p2 = d3.json('static/json/visitAvg.json');

var searchCode = "NPSA"
var lookupKey = -1 

parkChartData = []

// read thorugh the json files
var complete = Promise.all([p1, p2]);

complete.then((dat) => {
    //extract data
    var [geo, parks] = dat;

    for (var key in parks.park_code) {
        if (parks.park_code[key] = searchCode) {
            lookupKey = key
            break;
        }
    }

    var parkChartData = []
    var parkAvg = parks.avg_monthly[key]

    for (var datakey in parks) {
        if (datakey != "park_code" && datakey != "avg_monthly" && datakey != "great_month") {
            monvalue = datakey.split("_")[1].toUpperCase()
            parkVisit = parks[datakey][key]
            parkChartData.push({category: monvalue, value: parkVisit})
        }
    }
    // console.log(parkChartData)
    am4core.ready(function () {

        // Themes begin
        am4core.useTheme(am4themes_animated);
        // Themes end
    
        // Create chart instance
        var chart = am4core.create("chartdiv", am4charts.RadarChart);
        
        chart.scrollbarX = new am4core.Scrollbar();
    
        var data = [];
        // assign the park data
        data = parkChartData;
    
        // for (var i = 1; i < 13; i++) {
        //     data.push({ category: i, value: Math.round(Math.random() * 100) });
        // }
    
        chart.data = data;
        chart.radius = am4core.percent(100);
        chart.innerRadius = am4core.percent(50);
    
        // Create axes
        var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
        categoryAxis.dataFields.category = "category";
        categoryAxis.renderer.grid.template.location = 0;
        categoryAxis.renderer.minGridDistance = 30;
        categoryAxis.tooltip.disabled = true;
        categoryAxis.renderer.minHeight = 110;
        categoryAxis.renderer.grid.template.disabled = true;
        //categoryAxis.renderer.labels.template.disabled = true;
        let labelTemplate = categoryAxis.renderer.labels.template;
        labelTemplate.radius = am4core.percent(-80);
        labelTemplate.location = 0.5;
        labelTemplate.relativeRotation = 90;
    
        var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
        valueAxis.renderer.grid.template.disabled = true;
        valueAxis.renderer.labels.template.disabled = true;
        valueAxis.tooltip.disabled = true;
    
        // Create series
        var series = chart.series.push(new am4charts.RadarColumnSeries());
        series.sequencedInterpolation = true;
        series.dataFields.valueY = "value";
        series.dataFields.categoryX = "category";
        series.columns.template.strokeWidth = 0;
        series.tooltipText = "{valueY}";
        series.columns.template.radarColumn.cornerRadius = 10;
        series.columns.template.radarColumn.innerCornerRadius = 0;
    
        series.tooltip.pointerOrientation = "vertical";
    
        // on hover, make corner radiuses bigger
        let hoverState = series.columns.template.radarColumn.states.create("hover");
        hoverState.properties.cornerRadius = 0;
        hoverState.properties.fillOpacity = 1;
    
    
        series.columns.template.adapter.add("fill", function (fill, target) {
            return chart.colors.getIndex(target.dataItem.index);
        })
    
        // Cursor
        chart.cursor = new am4charts.RadarCursor();
        chart.cursor.innerRadius = am4core.percent(50);
        chart.cursor.lineY.disabled = true;
    
    }); // end am4core.ready()
});



