const express = require('express')
require('dotenv').config()

 const pool = require ('./src/database/postregres')
const app = express()

app.use(express.json())

app.get('/', async (req, res) => {

  try {

    const result = await pool.query('SELECT NOW()')

    res.json({
      status: 'ONLINE',
      banco: result.rows[0]
    })

  } catch (error) {

    res.status(500).json({
      erro: error.message
    })

  }

})

app.listen(process.env.PORT, () => {
  console.log(`Servidor rodando na porta ${process.env.PORT}`)
})