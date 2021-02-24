// Always have 3 cells per row
const NUM_OF_CELLS = 3

function toggleLogin () {
  // get elements of DOM
  const btn = document.getElementById('log-in')
  const add = document.getElementById('add')
  const save = document.getElementById('save')
  const displaybtn = document.getElementById('display')
  const remove = document.getElementById('remove')

  // Hide log-in
  btn.style.display = 'none'
  // display main feature dropdowns
  add.style.display = 'inline'
  save.style.display = 'inline'
  remove.style.display = 'inline'
  displaybtn.style.display = 'inline'
  // display add/remove buttons 
  document.getElementById('added-list').style.display = 'block'
  document.getElementById('button-row').style.display = 'inline-flex'
}

// Takes current option value - adds it to table
function addClass () {
  // get Course Dropdown
  const courseOption = document.getElementById('courses')
  // save Course selected
  const cVal = courseOption.options[courseOption.selectedIndex].value
  // get Term Dropdown
  const termOption = document.getElementById('terms')
  // save Term selected
  const tVal= termOption.options[termOption.selectedIndex].value
  // get Year Dropdown
  const yearOption = document.getElementById('year')
  // save Year selected
  const yVal = yearOption.options[yearOption.selectedIndex].value
  // access table in DOM
  const table = document.getElementById('course-rows')
  
  // if Trying to add dummy value - display not an option
  if (cVal === 'Course Name' || tVal === 'Term' || yVal === 'Year') {
     alert("Not an Available Option :)");
  } else {
    // else insert new row
    const row = table.insertRow()
    // assign class
    row.className = 'table-warning' // Example of how to set Bootstrap class dynamically
    // always add 3 cells as only inserting choice, term and year
    for (let x = 0; x < NUM_OF_CELLS; x++) {
    // insert new cell into row - 0 indexed
      table.rows[table.rows.length - 1].insertCell()
    }
    const currRow = table.rows[table.rows.length - 1].cells
    // Set each cell to correct value;
    currRow[0].textContent = cVal
    currRow[1].textContent = tVal
    currRow[2].textContent = yVal
  }
}

function removeClass () {
  // get Course Dropdown
  const courseOption = document.getElementById('courses')
  // save Course selected
  const cVal = courseOption.options[courseOption.selectedIndex].value
  // get Term Dropdown
  const termOption = document.getElementById('terms')
  // save Term selected
  const tVal= termOption.options[termOption.selectedIndex].value
  // get Year Dropdown
  const yearOption = document.getElementById('year')
  // save Year selected
  const yVal = yearOption.options[yearOption.selectedIndex].value
  // access table in DOM
  const table = document.getElementById('course-rows')
  // get # of rows
  const len = table.rows.length
  // if the table isn't empty
  if (len > 0) {
    let found = false
    let idx = 0
    // until found or gone through entire table
    while (!found && idx < len) {
    // get current row cell's values
      const currRow = table.rows[idx].cells
      // compare if this row is the correct one
      if (currRow[0].innerText === cVal && currRow[1].innerText === tVal && currRow[2].innerText === yVal) {
        found = true
        // set bool and delete row
        table.deleteRow(idx)
      } else { idx++ }
    }
  }
}


