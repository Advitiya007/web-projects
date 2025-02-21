
// let par=document.querySelector('  .cont')

function createflower(){
 let flower=document.createElement('div')

 flower.classList.add("flower")
 //the class list of this is imp
//chnaged name nothing happened

 //hegh twirtdh coklor prope specifiey
 //append chikld site interval create flwower 
 //remove 
 //animatuon flower translate 

flower.style.right=Math.random()*100 + '10vw'
flower.style.left=Math.random()*100 + 'vw'

    flower.style.top=Math.random()*10 + 'vw'
// flower.style.backgroundColor

const size= Math.random()*20+ 10
flower.style.height= `${size}px`
flower.style.width= `${size}px`
// flower.style.backgroundImage='url(https://i.pinimg.com/736x/60/48/8c/60488ce29af9a18dd08e00b272a93d14.jpg)'
// flower.style.borderRadius= `{($size-50)/20}px`

document.querySelector(".cont").appendChild(flower)

flower.animate(
    [
        //keyframes
       { transform:"translateY(0px)"},
       { transform:"translateY(400px)"},
       { transform:"translateX(0px)"},

    //    { transform:"translateX(-200px)"},

    ],
    
    //durations iterations
    {
   duration: Math.random()*3000+2000,
   iterations:1,
    easing:"linear",
    fill:"forwards"
    }
);



setTimeout(() => {
flower.remove();
}, 2000);

}

setInterval(createflower, 400);
