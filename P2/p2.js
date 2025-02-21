a = document.querySelectorAll(".item")
console.log(a);

b= document.querySelector('.bg')
console.log(b);



    a.forEach((item,index) =>{

    item.addEventListener('click',function(){
      const images=[
        'https://i.etsystatic.com/37360395/r/il/cf1922/4214068905/il_1140xN.4214068905_4rch.jpg',
'https://i.etsystatic.com/37360395/r/il/e0de5a/4172312469/il_1140xN.4172312469_o9nf.jpg',
'https://i.etsystatic.com/13086052/r/il/515fef/979909944/il_1140xN.979909944_34qg.jpg',
//736x/aa/03/2a/aa032a54fe4ee684b48589af84758b04.jpg'
'https://s44650.pcdn.co/wp-content/uploads/2023/07/melbourne-1200-1647052340.jpg',
'https://s44650.pcdn.co/wp-content/uploads/2023/07/london-1200-1647052305.jpg',
'https://i.etsystatic.com/34857934/r/il/f9bcc0/3784845913/il_1140xN.3784845913_1vr3.jpg'
       
      ]
      b.style.backgroundImage=`url('${images[index]}' )`
      b.style.backgroundSize="cover";
        console.log(`the image is selected ${index+1}`);
        
    })




})






// child2.forEach( (child)=> {
//     child.addEventListener(
//     'mouseover',function(){
        
//         console.log("hey");
        
// document.body.style.backgroundColor="slateblue"
//     }
// )