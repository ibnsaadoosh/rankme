var mongoose = require('mongoose');
var resumeSchema = require('./resume');
var jobSchema = new mongoose.Schema({
    title:
    {
        type: String,
        required: true,
        default: "job title"
    },
    description:
    {
        type: String,
        required: true,
        default: "job description"
    },
    resumes: [resumeSchema],
    userID: 
    {
        type: String,
        required: true
    }
});

var Jobs = mongoose.model('Job', jobSchema);

module.exports = Jobs;