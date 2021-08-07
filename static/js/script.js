setTimeout(() => {
   document.querySelector('#msg').style.display = 'none'
}, 3000)

const itens = document.querySelectorAll('.itens')

itens.forEach( (item) => {

    item.addEventListener('click', () => {
       if(item.style.textDecoration == ''){ 
         item.style.textDecoration = 'line-through'
         item.style.backgroundColor = '#EDD7CE'
        } else {
         item.style.textDecoration = ''
         item.style.backgroundColor = '#fff'
        }
   })
})

let inputItem = document.querySelector('#item')
let btnAdd = document.querySelector('#add')

btnAdd.disabled = true

inputItem.addEventListener('keyup', () => { 
   if(inputItem.value == '' || inputItem.value == undefined || inputItem.value == null) {
      btnAdd.disabled = true
   } else {
      btnAdd.disabled = false
   }
})