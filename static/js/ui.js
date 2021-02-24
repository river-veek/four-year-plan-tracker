const NUM_OF_CELLS = 3

function toggleShow () {
  document.getElementById('dropdown-list').classList.toggle('show')
}

function toggleLogin () {
  // get elements of DOM
  const btn = document.getElementById('log-in')
  const add = document.getElementById('add')
  const save = document.getElementById('save')
  const displaybtn = document.getElementById('display')
  const remove = document.getElementById('remove')
  // create source elements - set buttons to appear - set log in to disappear
  //createLists()
  btn.style.display = 'none'
  add.style.display = 'inline'
  save.style.display = 'inline'
  remove.style.display = 'inline'
  displaybtn.style.display = 'inline'
  document.getElementById('added-list').style.display = 'block'
  document.getElementById('button-row').style.display = 'inline-flex'
}

/*
function createLists () {
  // create source buttons / toggle log in
  createCourseList()
  createTermList()
  createYearList()
  document.getElementById('added-list').style.display = 'block'
}
*/
// Takes current option value - adds it to table
function addClass () {
	
  const course_opt = document.getElementById('courses')
  const c_option = course_opt.options[course_opt.selectedIndex].value
  const term_opt = document.getElementById('terms')
  const t_option = term_opt.options[term_opt.selectedIndex].value
  const y_opt = document.getElementById('year')
  const y_option = y_opt.options[y_opt.selectedIndex].value
  const table = document.getElementById('course-rows')
 
  if(c_option === 'Course Name' || t_option === 'Term' || y_option === 'Year') {
	// dont do anything
	// will impliment a pop up possibly or show warning not an option
  }
  else {
    // insert new row
    var row = table.insertRow()
    row.className = "table-warning"    // Example of how to set Bootstrap class dynamically
    // always add 3 cells as only inserting choice, term and year
    for (let x = 0; x < NUM_OF_CELLS; x++) {
    // insert new cell into row - 0 indexed
      table.rows[table.rows.length - 1].insertCell()
    }
    const currRow = table.rows[table.rows.length - 1].cells
    // Set each cell to correct value;
    currRow[0].textContent = c_option
    currRow[1].textContent = t_option
    currRow[2].textContent = y_option
    console.log(table.rows.length)
  }
}

function removeClass () {
  // get the current option values selected
  const course_opt = document.getElementById('courses')
  const c_option = course_opt.options[course_opt.selectedIndex].value
  const term_opt = document.getElementById('terms')
  const t_option = term_opt.options[term_opt.selectedIndex].value
  const y_opt = document.getElementById('year')
  const y_option = y_opt.options[y_opt.selectedIndex].value
  const currTable = document.getElementById('course-rows')
  
  const len = currTable.rows.length
  console.log(len)
  if(len > 0) {
    let found = false
    let idx = 0
    while (!found && idx < len) {
      const currRow = currTable.rows[idx].cells

      if (currRow[0].innerText === c_option && currRow[1].innerText === y_option && currRow[2].innerText === t_option) {
        found = true
        currTable.deleteRow(idx)
       } else { idx++ }
     }
   }
}
// Builds course list for now - used for testing
function createCourseList () {
  const classesList = ['Courses', '210: Computer Science I', '211: Computer Science II', '212: Computer Science III', '313: Intermediate Data Structures', '314: Computer Organization',
    '315: Intermediate Algorithms', '322: Introduction to Software Engineering', '330: C/C++ & Unix', '399: Applied Cryptography']
  const list = document.createElement('select')
  list.name = 'Courses'
  list.id = 'choice-list'
  list.class = 'c-list'
  for (const val of classesList) {
    const option = document.createElement('option')
    option.value = val
    option.text = val
    list.appendChild(option)
  }
  document.getElementById('main-space').appendChild(list)
}
// Builds term list for now - used for testing
function createTermList () {
  const termList = ['Terms', 'Fall', 'Winter', 'Spring', 'Summer']
  const tlist = document.createElement('select')
  tlist.name = 'Term'
  tlist.id = 'term-list'
  tlist.class = 't-list'

  for (const val of termList) {
    const option = document.createElement('option')
    option.value = val
    option.text = val
    tlist.appendChild(option)
  }
  document.getElementById('main-space').appendChild(tlist)
}
// Builds year list for now - used for testing
function createYearList () {
  const yearList = ['Year', '1st', '2nd', '3rd', '4th', '5th']
  const ylist = document.createElement('select')
  ylist.name = 'Year'
  ylist.id = 'year-list'
  ylist.class = 'y-list'

  for (const val of yearList) {
    const option = document.createElement('option')
    option.value = val
    option.text = val
    ylist.appendChild(option)
  }
  document.getElementById('main-space').appendChild(ylist)
}
