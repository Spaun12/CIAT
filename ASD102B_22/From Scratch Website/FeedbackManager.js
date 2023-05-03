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