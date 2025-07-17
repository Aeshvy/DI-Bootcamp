const knex = require('knex');
const dotenv = require('dotenv');
dotenv.config();

// const PGHOST='ep-summer-bush-a2hjoewn-pooler.eu-central-1.aws.neon.tech'
// const PPGDATABASE='neondb'
// const PGUSER='neondb_owner'
// const PGPASSWORD='npg_xoJgkrE0uL9Y'

const { PGHOST, PPGDATABASE, PGUSER, PGPASSWORD } = process.env;

const db = knex({
    client: 'pg',
    connection: {
        host: PGHOST,
        database: PPGDATABASE,
        user: PGUSER,
        password: PGPASSWORD,
        port: 5432,
        ssl: { rejectUnauthorized: false },
    }
});

db.select('id', 'name', 'price').from('products')
    .where('price', '>', 100)
    .orderBy('price', 'desc')
    .limit(5)
    .then(rows=> {
        console.log(rows);
    })

//     .catch(err=> {
//         console.log(err)
//     })
///////////////////////////////////////////////////////
// db('products')
//     .insert({
//         name: 'iPhone 15', price: 1200,})
//         .returning('*')

//         .then((data) => {
//             console.log('Product inserted:', data);
//         })

//         .catch((err) => {
//             console.error('Error inserting product:', err);
//         })
////////////////////////////////////////////////////////
// db.raw('SELECT * FROM products')
//     .then((data) => {
//         console.log('Products:', data.rows);
//     })
//     .catch((err) => {
//         console.error('Error fetching products:', err);
//     })
