export const state = () => ({
    completed: []
})

export const getters = {
}

export const mutations = {
    completeChall(state, id) {
        state.completed.push(id)
    }
}
