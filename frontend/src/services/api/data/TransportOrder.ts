export enum WaypointType {
    Pickup = 'PICKUP',
    Delivery = 'DELIVERY',
}

export interface Waypoint {
    id?: string

    address: string
    waypoint_type: WaypointType
}

export interface TransportOrder {
    id?: string
    date: string
    order_number: string
    customer_name: string
    waypoints: Waypoint[]
}
