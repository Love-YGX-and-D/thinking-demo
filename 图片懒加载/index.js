window.onload=function () {
    //搜索框
    let search=document.querySelector("div.search");
    let back=document.querySelector("main.back");
    let son=document.querySelectorAll(" main.smallBox .son");
    //滚动条高度+浏览器高度 > 楼层section的高度
    //获取浏览器高度
    let Height=window.innerHeight;
    let floor=document.querySelectorAll("section.floor");
    let arr=[];
    floor.forEach(function (value) {
        arr.push(value.offsetTop);
    })
    window.onscroll=function () {
        let gunHeight=document.body.scrollTop || document.documentElement.scrollTop;
        arr.forEach(function (value, index) {
            let imgs=floor[index].querySelectorAll("img");
            if(gunHeight+Height>value+300){
                son.forEach(function (value1) {
                    value1.classList.remove("son1")
                })
                imgs.forEach(function (v) {
                    v.src=v.getAttribute("imgsrc");
                })
                son[index].classList.add("son1")
            }
        })
        if(gunHeight>Height){
            animate(search,{top:0},120)
            // search.style.top=0;
        }
        else{
            animate(search,{top:-80},120)
            // search.style.top=-80+"px";
        }
        son.forEach(function (value,index) {
            value.onmouseenter=function () {
                value.style.cursor="pointer";
            }
            value.onclick=function () {
                animate(document.documentElement,{scrollTop:arr[index]},120);
                animate(document.body,{scrollTop:arr[index]},120)
            }
        })
    }
    back.onclick=function () {
        animate(document.body,{scrollTop:0},200);
        animate(document.documentElement,{scrollTop:0},120);
    }
    back.onmouseenter=function () {
        back.style.cursor="pointer";
    }

}