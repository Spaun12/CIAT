// Michael D. Connell Jr. Beginner Website creation project 2023 CIAT WebDevelopment
// Need to do a bit more research on this one. Want to know best practices for this type of code.

export default class FeedbackManager {
    constructor() {
        this.selectedOptions = [];
    }

    addOption(option) {
        this.selectedOptions.push(option);
    }

    removeOption(option) {
        const index = this.selectedOptions.indexOf(option);
        if (index > -1) {
            this.selectedOptions.splice(index, 1);
        }
    }

    isSelected(option) {
        return this.selectedOptions.includes(option);
    }

    toString() {
        return JSON.stringify(this.selectedOptions);
    }

    isEmpty() {
        return this.selectedOptions.length === 0;
    }
}