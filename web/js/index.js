$.getJSON('./files/data.json', function (data) {
  // retrieve the json
  var catids = new Set();
  var catg = new Set();
  var companies = new Array();
  var company_dict = {};
  for (i = 0; i < data.length; i++) {
    catids.add(data[i].category_id);
    catg.add(data[i].category_name);
    if (
      company_dict[data[i].category_name] === undefined ||
      company_dict[data[i].category_name] === null
    ) {
      company_dict[data[i].category_name] = [data[i].company_name];
    } else {
      company_dict[data[i].category_name].push(data[i].company_name);
    }
  }
  console.log(company_dict);
  // update the html
  var catarr = [...catg]; /// convert set to array
  for (i = 1; i < catarr.length + 1; i++) {
    document.getElementById('cat-' + i).innerHTML = catarr[i - 1];
    document.getElementById('collapse-' + i).innerHTML =
      "<ul id='complist-" + i + "' style='list-style-type:circle;'>";
    for (j = 0; j < company_dict[catarr[i - 1]].length; j++) {
      console.log(i);
      var elm = document.createElement('li');
      var atag = document.createElement('a');
      atag.innerHTML = company_dict[catarr[i - 1]][j];
      atag.href = '#';
      elm.appendChild(atag);
      document.getElementById('complist-' + i).appendChild(elm);
    }
  }
});
