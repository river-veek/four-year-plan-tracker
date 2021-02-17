function toggleShow (){
  document.getElementById('dropdown-list').classList.toggle('show')
}
function classInfo (id) {
	toggleShow ()
	var currentSpace = document.getElementById('init')
	var matrix = NaN
	document.body.insertBefore(matrix, currentSpace);
}
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    const dropdowns = document.getElementsByClassName('dropdown-content')
    for (let i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i]
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show')
      }
    }
  }
}
