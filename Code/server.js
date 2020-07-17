const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

app.get('/', (req, res) => res.send('Hello World!'));

app.use(express.static('public'));

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'prateek@database',
  database: 'vmasc',
});

app.listen(PORT, () => console.log(`Server started on port:${PORT}`));

//Api for getting all categories and companies
app.get('/categories&companies', (req, res) => {
  connection.query(
    'SELECT cat.category_name, cat.category_id, c.company_name, cn.company_stocknews, company_stocklink, cs. company_stock_price FROM categories cat,companies c,company_news cn,company_stocks cs WHERE cat.category_id = c.category_id and c.company_id = cn.company_id and cn.company_id = cs.company_id;',
    (err, rows, fields) => {
      if (!err) res.send(rows);
      else console.log(err);
    }
  );
});

//connection.connect(function (err) {
//if (err) throw err;
//connection.query('SELECT * from categories', function (err, result, fields) {
//if (err) throw err;
//console.log(result);
//});
//});
