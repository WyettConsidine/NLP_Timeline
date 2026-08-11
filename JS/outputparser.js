function test() {
    document.getElementById('button').style.backgroundColor = "rgb(252, 5, 5)";
    document.getElementById("output").innerHTML = "hehe"
}
async function getJSON() {
    const response = await fetch ("../JSON_Output/TrauntTest.json")
    const data = await response.json();
    console.log(data);
}

async function makeCard(){ //Takes a chosen amount of array indexes and prints out their Date, Text and File
    const response = await fetch ("../JSON_Output/TrauntTest.json")
    const data = await response.json();
    let text = "";
    for (i = 0; i < 4; i++) {
        text += "<li>" + data[i].Date + data[i].Text + "[" + data[i].File + "]"+"</li>";
        document.getElementById("output").innerHTML = text;
        console.log(text);
    }
}
