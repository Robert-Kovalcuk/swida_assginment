<template>
    <div class="item__wrapper">
        <div class="item__header">
            <h3>order no. {{ props.order.order_number }}</h3>
            <p>{{ props.order.customer_name }}</p>
            <button @click="toggleExpandable">expand</button>
        </div>
        <div v-show="isExpanded" class="item__expandable">
            <p>date: {{ props.order.date }}</p>
            <div v-for="(waypoint, index) in props.order.waypoints" :key="index">
                <p>address: {{ waypoint.address }}</p>
                <p>type: {{ waypoint.waypoint_type }}</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>

	import type { TransportOrder } from '@/services/api/data/TransportOrder.ts'
	import { computed, ref } from 'vue'

	const props = defineProps<{
		order: TransportOrder
	}>()

	const isExpanded = ref(false)

	const toggleExpandable = () => {
		isExpanded.value = !isExpanded.value
	}

	const headerBorder = computed(() => isExpanded.value ? '1px solid #ccc' : 'none')

</script>

<style scoped>
.item__wrapper {
    display: flex;
    flex-direction: column;
    cursor: pointer;
    padding: 0.225rem;
    border: 1px solid #ccc;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.item__header {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    justify-content: space-between;
    border-bottom: v-bind(headerBorder);
    width: 100%;
}

.item__expandable {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;

    div {
        display: flex;
        gap: 0.5rem;
    }
}
</style>
