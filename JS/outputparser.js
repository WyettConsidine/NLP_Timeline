function test() {
    document.getElementById('button').style.backgroundColor = "rgb(252, 5, 5)";
    document.getElementById("output").innerHTML = "hehe"
}
async function getJSON() {
    const response = await fetch ("../JSON_Output/TrauntTest.json")
    const data = await response.json();
    console.log(data);
}
// currently pulls out 3 indexes from the array. Need to find a way to access those as objects
async function makeCard(){
    const response = await fetch ("../JSON_Output/TrauntTest.json")
    const data = await response.json();
    let text = "";
    for (i = 0; i < 4; i++) {
        text += "<li>" + data[i].Date + data[i].Text + data[i].File + "</li>";
        document.getElementById("output").innerHTML = text;
        console.log(text);
    }
}
