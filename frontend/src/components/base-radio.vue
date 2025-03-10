<template>
    <div class="radio">
        <label v-for="(v) in props.values" :key="v" class="inputs-label-wrapper">
            <input
                v-model="value"
                :value="v"
                type="radio"
                @change="value = v"
            >
            <span class="label__span">{{ v }}</span>
        </label>
    </div>
</template>

<script lang="ts" setup>
	const props = defineProps<{
		values: string[],
	}>()

	const value = defineModel<string>('input', {
		required: true,
	})
</script>

<style scoped>
.radio {
    display: flex;
    gap: 0.5rem;
    width: 100%;

}

.inputs-label-wrapper {
    display: flex;
    gap: 0.755rem;
    font-size: 14px;

    input {
        cursor: pointer;
        accent-color: #2c3e50;
    }
}
</style>
