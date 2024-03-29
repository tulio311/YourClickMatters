let caja1 = document.getElementById('box1');
let caja2 = document.getElementById('box2');
let caja3 = document.getElementById('box3');
let caja4 = document.getElementById('box4');


function req(color, word){
    
    $.ajax({
        url: "http://127.0.0.1:5000/receive",
        //url: "https://www.hittite-imhotep.com/",
        type: "POST", // Can be POST, PUT, DELETE, etc.
        dataType: "json", // Expected data format (json, html, etc.)
        data:{
            color: color,
            word: word
        },
        success: function(data) {
          console.log("Success! Data:", data);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.error("Error! Status:", textStatus, errorThrown);
        }
      });

}


function f1(){
    let color = 'Black';
    let word = document.getElementById('word1').innerHTML;
    req(color,word);
    console.log(color + word);
}
function f2(){
    let color = 'Blue';
    let word = document.getElementById('word2').innerHTML;
    req(color,word);
    console.log(color + word);
}
function f3(){
    let color = 'Green';
    let word = document.getElementById('word3').innerHTML;
    req(color,word);
    console.log(color + word);
}
function f4(){
    let color = 'Red';
    let word = document.getElementById('word4').innerHTML;
    req(color,word);
    console.log(color + word);
}

caja1.addEventListener('click',f1);
caja2.addEventListener('click',f2);
caja3.addEventListener('click',f3);
caja4.addEventListener('click',f4);

