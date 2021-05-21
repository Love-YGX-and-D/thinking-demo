window.onload=function () {
    let Box1=document.querySelectorAll("div.box .box1");   //5个小盒子盒子
    let box=document.querySelector("div.box");            //大盒子
    let Width=parseInt(getComputedStyle(box,null).width);   //小盒子的宽度
    let Left=document.querySelector("div.box .left");    //左右两个盒子
    let Right=document.querySelector("div.box .right");
    let circle=document.querySelector("div.box .circle");  //小圆圈
    let Son=document.querySelectorAll("div.box .circle .son");//小点
    console.log(Box1,Width,Left,Right,Son);
    let now=0;
    let next=0;
    flag=true;
    let t=setInterval(move2,2000);
    //右向左
    function move2() {
        next++;
        if(next==Box1.length){
            next=0;
        }
        // 就绪
        Son[next].classList.add("son1");
        Son[now].classList.remove("son1");
        Box1[next].style.left=Width+"px";
        //动画
        animate(Box1[next],{left:0});
        animate(Box1[now],{left:-Width},function () {
            flag=true;
        });
        now=next;
    }
    //左向右
    function move3() {
        next--;
        if(next<0){
            next=Box1.length-1;
        }
        //就绪
        Box1[next].style.left=-Width+"px";
        Son[next].classList.add("son1");
        Son[now].classList.remove("son1");
        //动画
        animate(Box1[next],{left:0});
        animate(Box1[now],{left:Width},function () {
            flag=true;
        });
        now=next;
    }
    box.onmouseenter=function () {
        clearInterval(t);
    }
    box.onmouseleave=function () {
        t=setInterval(move2,2000)
    }
    Left.onclick=function () {
        if(flag==false){
            return;
        }
        if(next==0){
            return;
        }
        flag=false;
        move3();
    }
    Right.onclick=function () {
       if(flag==false){
            return;
        }
        if(next==Box1.length-1){
            return;
        }
        flag=false;
        move2();
    }
    Son.forEach(function(value,index){
        value.onclick=function(){
            if(index==now){
                return;
            }
            else if(index>now){
                Son[index].classList.add("son1");
                Son[now].classList.remove("son1");
                //就绪
                Box1[now].style.left=-Width+"px";
                Box1[index].style.left=0;
            }
            else if(index<now){
                Son[index].classList.add("son1");
                Son[now].classList.remove("son1");
                //就绪
                Box1[now].style.left=Width+"px";
                Box1[index].style.left=0+"px";
            }
            now=next=index;
        }
    })
}