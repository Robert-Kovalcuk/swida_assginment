<template>
    <div class="home__wrapper">
        <h1>Create transport order</h1>

        <form class="create-order_form" @submit.prevent="submit">
            <base-input v-model:input="newTransportOrder.customer_name"
                        label="Enter customer name"
                        type="text"/>
            <base-input v-model:input="newTransportOrder.order_number"
                        label="Enter order number"
                        type="text"/>

            <base-input v-model:input="newTransportOrder.date"
                        label="Enter date"
                        type="date"/>

            <div class="waypoints__container">
                <h2>Waypoints</h2>
                <div class="waypoints_items__wrapper">
                    <div v-for="(waypoint, index) in newTransportOrder.waypoints" :key="index"
                         class="waypoint_item">
                        <button v-if="(index !== 0 && index !== 1)" type="button"
                                @click="removeWaypoint(index)">X
                        </button>
                        <base-input v-model:input="waypoint.address"
                                    label="Enter waypoint address" type="text"
                        />
                        <base-radio v-model="waypoint.waypoint_type"
                                    :input="newTransportOrder.waypoints[index].waypoint_type"
                                    :values="waypointTypes"
                                    header="Waypoint type"/>
                    </div>
                    <button type="button" @click="addWaypoint">+</button>
                </div>
            </div>
            <button type="submit">Submit</button>
        </form>

        <h1>Transport orders</h1>
        <base-input v-model:input="customerNameFilter" label="filter on customer name" type="text"/>
        <button type="button" @click="fetchTransportOrders">Filter</button>
        <div v-if="orders.length" class="orders__list">
            <expandable-transport-order-item v-for="order in orders"
                                             :key="order.id" :order="order"/>
        </div>
        <h4 v-else>No transport orders</h4>
    </div>
</template>

<script lang="ts" setup>
	import { onMounted, reactive, ref } from 'vue'
	import {
		type TransportOrder,
		type Waypoint,
		WaypointType,
	} from '@/services/api/data/TransportOrder.ts'
	import BaseRadio from '@/components/base-radio.vue'
	import BaseInput from '@/components/base-input.vue'
	import TransportOrdersService from '@/services/api/transportOrdersService.ts'
	import ExpandableTransportOrderItem from '@/components/expandable-transport-order-item.vue'

	const newTransportOrder = reactive<TransportOrder>({
		date: '2025-01-01',
		order_number: '123213123',
		customer_name: 'John Doe',
		waypoints: [{
			address: 'Street 1',
			waypoint_type: WaypointType.Pickup,
		}, {
			address: 'Street 2',
			waypoint_type: WaypointType.Delivery,
		}],
	})

	const waypointTypes = Object.values(WaypointType)
	const orders = ref<TransportOrder[]>([])
	const customerNameFilter = ref('')

	onMounted(() => {
		fetchTransportOrders()
	})

	async function submit() {
		if (newTransportOrder.waypoints.length < 2) {
			alert('You need to have at least 2 waypoints')
			return
		}

		if (!newTransportOrder.waypoints.some((w: Waypoint) => w.waypoint_type === WaypointType.Pickup)) {
			alert('You need to have at least one pickup waypoint')
			return
		}

		if (!newTransportOrder.waypoints.some((w: Waypoint) => w.waypoint_type === WaypointType.Delivery)) {
			alert('You need to have at least one delivery waypoint')
			return
		}

		try {
			const result = await TransportOrdersService.createTransportOrder(newTransportOrder)

			if (isSuccess(result)) {
				alert(`Transport order: ${result.order_number} created`)
				fetchTransportOrders()
			} else
				alert(`Error creating transport order ${JSON.stringify(result)}`)

		} catch (error) {
			alert(`Error creating transport order ${error}`)
		}
	}

	function addWaypoint() {
		newTransportOrder.waypoints.push({
			address: '',
			waypoint_type: WaypointType.Pickup,
		})
	}

	function removeWaypoint(index: number) {
		newTransportOrder.waypoints.splice(index, 1)
	}

	function fetchTransportOrders() {
		TransportOrdersService.getTransportOrders(customerNameFilter.value).then((res) => {
			orders.value = res
		})
	}

	function isSuccess(result: unknown): result is { id: string } {
		return typeof result === 'object' && result !== null && 'id' in result
	}


</script>

<style scoped>

.home__wrapper {
    width: 100%;

    h1 {
        margin-top: 2rem;
    }
}

.create-order_form {
    display: flex;
    flex-direction: column;
    gap: 1rem;

    button[type="submit"] {
        margin-top: 2rem;
        padding: 1rem;
    }
}

.waypoints__container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 2rem;
}

.waypoints_items__wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    width: 100%;

    .waypoint_item {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        width: inherit;
        padding: 1rem;
        border: 1px solid #f0f0f0;
        border-radius: 0.25rem;

        button {
            align-self: end;
            background-color: red;
            color: white;
            border: none;
            width: 50%;
            max-width: 2rem;
            border-radius: 0.25rem;
            cursor: pointer;
        }
    }

    button {
        background-color: cornflowerblue;
        color: white;
        border: none;
        width: 50%;
        max-width: 6rem;
        border-radius: 0.25rem;
        cursor: pointer;
    }
}

.orders__list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
}
</style>
