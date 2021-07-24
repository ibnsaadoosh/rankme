var mongoose = require('mongoose');

var resumeSchema = new mongoose.Schema({
    filename:
    {
        type: String,
        required: true,
        default: "cv"
    },
    path:
    {
        type: String,
        required: true,
        default: "public/resumes"
    },
    percentage:
    {
        type: Number,
        required: true,
        default: Math.random()
    },
    jobId:
    {
        type: String,
        required: true
    }
});

module.exports = resumeSchema;