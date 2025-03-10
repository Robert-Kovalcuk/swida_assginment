<template>
    <label class="label">
        {{ props.label }}
        <input v-model="value" :type="props.type" required/>
    </label>
</template>

<script lang="ts" setup>

	import { defineModel } from 'vue'

	const props = defineProps<{
		type: 'text' | 'number' | 'tel' | 'email' | 'password' | 'date',
		label: string,
	}>()

	const value = defineModel('input', {
		type: String,
		default: '',
	})

</script>

<style scoped>
.label {
    display: flex;
    flex-direction: column;
    gap: 0.225rem;
    font-size: 1rem;
    font-weight: lighter;

    input {
        font-size: 1rem;
        padding: 0.5rem;
        border: none;
        border-radius: 0.25rem;
    }
}
</style>
