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
    tab1.innerHTML+='<tr><td><input type="number" id="x'+tab1var+'" /></td><td><input type="number" id="y'+tab1var+'" /></td><td id="random'+tab1var+'">'+rand1+'</td><td><select id="qtype'+tab1var+'"> <option value="i">input</option><option value="n">nothing</option><option value="o">output</option></select></td></tr>'
}

var plus2 = document.getElementById("buttonplus2");
var tab2=document.getElementById("tab2");
plus2.onclick=more2;
var tab2var=2;

function more2(){
    tab2.innerHTML+='<tr><td><input type="number" name="x1'+tab2var+'" /></td><td><input type="number" name="y1'+tab2var+'" /></td><td>---</td><td><input type="number" name="x2'+tab2var+'" /></td><td><input type="number" name="y2'+tab2var+'" /></td></tr>';
    tab2var ++;
}


//// sert a rien sauf pour presenter

var show2 =document.getElementById("buttonsend1");

async function allsend1(){
    const result = await senddata();
    display2();
}

show2.onclick=allsend1;

function display2(){
    document.getElementById("part2").style.display="flex";
}

var show3 =document.getElementById("buttonsend2");
show3.onclick=display3;
function display3(){
    document.getElementById("part3").style.display="flex";
}
