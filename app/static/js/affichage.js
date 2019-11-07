var plus1 = document.getElementById("buttonplus1");
var tab1= document.getElementById("tab1");
plus1.onclick=more1;
var tab1var=1;
function random8(){ 
    var random = Math.floor(Math.random() * 8);
    return random;
}
var rand1= random8();
document.getElementById("random1").innerHTML=rand1;


function more1(){
    rand1= random8();
    tab1var ++;
    var textTab= '<td><input type="number" min="0" max="100" id="x'+tab1var+'" /></td><td><input type="number" min="0" max="100" id="y'+tab1var+'" /></td><td id="random'+tab1var+'">'+rand1+'</td><td><select id="qtype'+tab1var+'"> <option value="i">input</option><option value="n">nothing</option><option value="o">output</option></select></td>';
    var newRow = document.createElement('TR');
    newRow.innerHTML = textTab;
    document.getElementById('tab1').appendChild(newRow);
}

var plus2 = document.getElementById("buttonplus2");
var tab2=document.getElementById("tab2");
plus2.onclick=more2;
var tab2var=0;

function more2(){
    const tabList = tabQubit();
    var options="";
    for(i=0;i<tabList.length;i++){
        options+='<option value="'+ tabList[i][0]+';'+ tabList[i][1]+'">Qubit ('+ tabList[i][0]+';'+ tabList[i][1]+')</option>';
    }
    
    var textTab ='<td><select id="tab21'+tab2var+'" />'+options+'</select></td><td>---</td><td><select id="tab22'+tab2var+'" />'+options+'</select></td>';
    var newRow = document.createElement('TR');
    newRow.innerHTML = textTab;
    document.getElementById('tab2').appendChild(newRow);
    
    tab2var ++;


}


var show2 =document.getElementById("buttonsend1");
show2.onclick=allsend1;

async function allsend1(){
    const result = await senddata();
    document.getElementById("part2").style.display="flex";
    // We add a first line by default.
    more2();
    document.getElementById('buttonplus1').style.display="none";
    document.getElementById('buttonsend1').style.display="none";
}


var show3 =document.getElementById("buttonsend2");
show3.onclick=display3;
async function display3(){
    document.getElementById("part3").style.display="flex";
    const result = await send_entanglement_graph();
    alert("Great, entanglement finished!")
}


