// Always have 3 cells per row
const NUM_OF_CELLS = 3

function toggleLogin (name) {
  // get elements of DOM
  const main = document.getElementById('main-space')
  const add = document.getElementById('add')
  const save = document.getElementById('save')
  const displaybtn = document.getElementById('display')
  const remove = document.getElementById('remove')
  const dInfo = document.getElementById('helperDropdownInfo')
  const tInfo = document.getElementById('helperTableInfo')

  // Update the display for what student has been selected
  const currStudentText = document.getElementById('currStudentText')
  const currStudent = document.getElementById('currStudent')

  // Set display fields
  currStudent.innerText = name
  currStudentText.innerText = "Current Student: "

  // Hide log-in
  main.style.display = 'none'

  // display main feature dropdowns
  add.style.display = 'inline'
  save.style.display = 'inline'
  remove.style.display = 'inline'
  displaybtn.style.display = 'inline'

  // display add/remove buttons
  document.getElementById('added-list').style.display = 'block'
  document.getElementById('button-row').style.display = 'inline-flex'
  dInfo.style.display = 'inline'
  tInfo.style.display = 'inline'
}

// Wrapper for main toggleLogin for when user inputs new student ID
function toggleLoginNew () {
  const input = document.getElementById('studentCreateInput').value
  return toggleLogin(input)
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

function saveTable() {
	const table = document.getElementById('course-rows')
	const len = table.rows.length
	// Array containing all the Rows
	var savedData = Array()
	for(let x = 0; x < len; x++)
	savedData.push([])
	console.log(savedData)
	// Clear table
	for(let x = 0; x < len; x++)
	{ table.deleteRow(0) }
}



