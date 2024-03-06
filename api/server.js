const express = require("express")
const mongoose = require("mongoose")
const cors = require("cors")

const app = express()

app.use(express.json())
app.use(express.urlencoded({extended:true}))
app.use(cors())

mongoose.connect("mongodb+srv://admin:v226tR8EqMj5AUwN@ballerbets.tjy50oc.mongodb.net/")
.then(() => {
    app.listen(4000, () => console.log("DB is listening at port 4000"))
})
.catch((error) => console.log(error.message))



