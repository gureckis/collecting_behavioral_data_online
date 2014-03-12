

function makeStage(w, h) {
	var stage = d3.select(".container")
				  .insert("center")
				  .insert("svg")
				  .attr("width", w)
				  .attr("height", h);
	return stage;
}

function drawStimulus(stage, cx, cy, radius, fillcolor) {
	stage.insert("circle")
		 .attr("cx", cx)
		 .attr("cy", cy)
		 .attr("r", radius)
		 .style("fill", fillcolor)
		 .style("stroke", "steelblue")
		 .style("stroke-width","5px");
}

function clearStimulus(stage) {
	stage.selectAll("circle").remove();
}

function clearButton() {
	d3.select(".container")
	  .selectAll("button").remove();
}

function makeButton(text, callback) {
	d3.select(".container")
		.insert("button")
		.attr("type", "button")
		.attr("class", "btn btn-primary btn-lg")
		.text(text)
		.on("click", function (d) { callback(); });
}

var trials = [
				{"color": "lightblue", "radius": 20}, // trial 1
				{"color": "yellow", "radius": 20}, // trial 2
				{"color": "red", "radius": 50}, // trial 3
				{"color": "blue", "radius": 20} // trial 4
			 ];

function doTrial(stage, stim_array) {
	if (stim_array.length > 0 ) {
		// do the trial
		var stim = stim_array.shift();
		clearStimulus(stage);
		clearButton();
		drawStimulus(stage, 300/2, 300/2, stim["radius"], stim["color"]);
		makeButton("Next trial", function () { doTrial(stage, stim_array); })

	} else  {
		alert("i'm done with experiment.");
	}
}


stage = makeStage(300, 300);
doTrial(stage, trials);