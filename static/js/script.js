let draw_input = document.getElementById('number_of_draws')
let system_input = document.getElementById('max_for_system')

function handleClick(cb) {
  if (cb.checked) {
    draw_input.setAttribute("disabled", '');
    system_input.removeAttribute("disabled");
  } else {
    draw_input.removeAttribute("disabled")
    system_input.setAttribute("disabled", '');
  }
}