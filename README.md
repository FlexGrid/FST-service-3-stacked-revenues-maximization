# OpenAPI server for the FLEXGRID System

## 1. Design your API using swagger editor

1. Use the online tool at https://editor.swagger.io/ to create the API
   definition.

2. As a starting point, use the swagger file like below:

    ```yml
    openapi: 3.0.3
    info:
      title: Flexgrid ATP API
      description: The Automated Trading Platform (ATP) of the flexgrid project
      termsOfService: https://atp.flexgrid-project.eu/terms/
      contact:
        name: Dimitros J. Vergados
        url: https://flexgrid-project.eu
      license:
        name: BSD
        url: https://github.com/pyeve/eve-swagger/blob/master/LICENSE
      version: "1.0"
    servers:
    - url: http://localhost:8080/
    tags:
    - name: Prosumer
    paths:
      /stacked_revenues:
        post:
          tags:
          - StackedRevenues (UCS 2.3)
          summary: Initiates a simulation scenario for Stacked Revenues maximization
          operationId: stacked_revenues_post
          requestBody:
            $ref: '#/components/requestBodies/StackedRevenuesParams'
          responses:
            "201":
              description: operation has been successful
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/StackedRevenuesResult'
            "400":
              description: bad request
          security:
          - MyTokenAuth: []
          x-openapi-router-controller: swagger_server.controllers.stacked_revenues_ucs23_controller
      /flex_offers:
        post:
          tags:
          - FlexOffers (UCS 4.3)
          summary: Creates a Flexibility Offser (FlexOffer) based of FlexAssets
          operationId: flex_offers_post
          requestBody:
            $ref: '#/components/requestBodies/FlexOfferParams'
          responses:
            "201":
              description: operation has been successful
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/FlexOfferResult'
            "400":
              description: bad request
          security:
          - MyTokenAuth: []
          x-openapi-router-controller: swagger_server.controllers.flex_offers_ucs43_controller
      /pricing:
        post:
          tags:
          - Pricing (UCS 4.2)
          summary: Creates an evaluation of various pricing mechanisms
          operationId: pricing_post
          requestBody:
            $ref: '#/components/requestBodies/PricingParams'
          responses:
            "201":
              description: operation has been successful
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/PricingResult'
            "400":
              description: bad request
          security:
          - MyTokenAuth: []
          x-openapi-router-controller: swagger_server.controllers.pricing_ucs42_controller
    components:
      schemas:
        StackedRevenuesParams:
          required:
          - country
          - markets
          - sdate
          - storage_units
          type: object
          properties:
            sdate:
              type: string
              format: date
            country:
              type: string
            markets:
              minItems: 1
              type: array
              items:
                type: string
                enum:
                - DAM
                - RM
                - FM
                - BM
            storage_units:
              minItems: 1
              type: array
              items:
                $ref: '#/components/schemas/StorageUnit'
        StackedRevenuesResult:
          required:
          - flex_offer
          - revenues
          - sdate
          type: object
          properties:
            sdate:
              type: string
              format: date
            flex_offer:
              $ref: '#/components/schemas/FlexOffer'
            revenues:
              $ref: '#/components/schemas/StackedRevenuesResultRevenues'
          example:
            sdate: 2000-01-23
            flex_offer:
            - balancing_market_offer_down: null
              q-LMPs:
                price_unit: €/MVar
                volume_unit: MVar
                values: null
              reserve_market_offer_down: null
              storage_unit: storage_unit
              balancing_market_offer_up: null
              day_ahead_market_offer:
                price_unit: €/MWh
                volume_unit: MWh
                values:
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
              reserve_market_offer_up:
                price_unit: €/MWh^2
                volume_unit: MWh^2
                values: null
              d-LMPs: null
            - balancing_market_offer_down: null
              q-LMPs:
                price_unit: €/MVar
                volume_unit: MVar
                values: null
              reserve_market_offer_down: null
              storage_unit: storage_unit
              balancing_market_offer_up: null
              day_ahead_market_offer:
                price_unit: €/MWh
                volume_unit: MWh
                values:
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
              reserve_market_offer_up:
                price_unit: €/MWh^2
                volume_unit: MWh^2
                values: null
              d-LMPs: null
            revenues:
              balancing_market_revenues: null
              reserve_market_revenues: null
              flexibility_market_revenues: null
              day_ahead_market_revenues:
                currency: €
                value: 1.4658129805029452
        FlexOfferParams:
          type: object
          properties:
            country:
              type: string
            flex_assets:
              minItems: 1
              type: array
              items:
                $ref: '#/components/schemas/FlexAsset'
            start_datetime:
              type: string
              format: date-time
            end_datetime:
              type: string
              format: date-time
            time_granularity:
              $ref: '#/components/schemas/FlexOfferParams_time_granularity'
            location:
              $ref: '#/components/schemas/Location'
            store_data:
              type: boolean
        FlexOfferResult:
          type: object
          properties:
            reserve_market_offer_up:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh2'
            reserve_market_offer_down:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh2'
            expected_revenues:
              $ref: '#/components/schemas/FlexOfferResult_expected_revenues'
          example:
            reserve_market_offer_down: null
            expected_revenues:
              currecy: currecy
              revenue_vector:
              - revenue: 0.8008281904610115
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
              - revenue: 0.8008281904610115
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
            reserve_market_offer_up:
              price_unit: €/MWh^2
              volume_unit: MWh^2
              values: null
        PricingParams:
          type: object
          properties:
            country:
              type: string
            start_datetime:
              type: string
              format: date-time
            end_datetime:
              type: string
              format: date-time
            time_granularity:
              $ref: '#/components/schemas/FlexOfferParams_time_granularity'
            time_frame_id:
              type: string
            flex_request:
              $ref: '#/components/schemas/FlexOffer'
            flex_assets:
              type: array
              items:
                $ref: '#/components/schemas/FlexAsset'
            storage_units:
              minItems: 1
              type: array
              items:
                $ref: '#/components/schemas/StorageUnit'
            curtailable_loads:
              type: array
              items:
                $ref: '#/components/schemas/CurtailableLoad'
            flex_contracts:
              type: array
              items:
                $ref: '#/components/schemas/FlexContract'
            profit_margin:
              type: number
            store_data:
              type: boolean
        PricingResult:
          type: object
          properties:
            flex_contracts:
              type: array
              items:
                $ref: '#/components/schemas/PricingResult_flex_contracts'
            users:
              type: array
              items:
                $ref: '#/components/schemas/PricingResult_aggregated_user_welfare'
          example:
            flex_contracts:
            - flex_contract:
                name: name
                id: 0.8008281904610115
                gamma: 6.027456183070403
              flexibility_revenues:
                currecy: currecy
                revenue_vector:
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
              flexibility:
              - balancing_market_offer_down: null
                q-LMPs:
                  price_unit: €/MVar
                  volume_unit: MVar
                  values: null
                reserve_market_offer_down: null
                storage_unit: storage_unit
                balancing_market_offer_up: null
                day_ahead_market_offer:
                  price_unit: €/MWh
                  volume_unit: MWh
                  values:
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                reserve_market_offer_up:
                  price_unit: €/MWh^2
                  volume_unit: MWh^2
                  values: null
                d-LMPs: null
              - balancing_market_offer_down: null
                q-LMPs:
                  price_unit: €/MVar
                  volume_unit: MVar
                  values: null
                reserve_market_offer_down: null
                storage_unit: storage_unit
                balancing_market_offer_up: null
                day_ahead_market_offer:
                  price_unit: €/MWh
                  volume_unit: MWh
                  values:
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                reserve_market_offer_up:
                  price_unit: €/MWh^2
                  volume_unit: MWh^2
                  values: null
                d-LMPs: null
              aggregated_user_welfare:
                currecy: currecy
                welfare_vector:
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
            - flex_contract:
                name: name
                id: 0.8008281904610115
                gamma: 6.027456183070403
              flexibility_revenues:
                currecy: currecy
                revenue_vector:
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
              flexibility:
              - balancing_market_offer_down: null
                q-LMPs:
                  price_unit: €/MVar
                  volume_unit: MVar
                  values: null
                reserve_market_offer_down: null
                storage_unit: storage_unit
                balancing_market_offer_up: null
                day_ahead_market_offer:
                  price_unit: €/MWh
                  volume_unit: MWh
                  values:
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                reserve_market_offer_up:
                  price_unit: €/MWh^2
                  volume_unit: MWh^2
                  values: null
                d-LMPs: null
              - balancing_market_offer_down: null
                q-LMPs:
                  price_unit: €/MVar
                  volume_unit: MVar
                  values: null
                reserve_market_offer_down: null
                storage_unit: storage_unit
                balancing_market_offer_up: null
                day_ahead_market_offer:
                  price_unit: €/MWh
                  volume_unit: MWh
                  values:
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                  - volume: 6.027456183070403
                    end_timestamp: 2000-01-23T04:56:07.000+00:00
                    start_timestamp: 2000-01-23T04:56:07.000+00:00
                    price: 0.8008281904610115
                reserve_market_offer_up:
                  price_unit: €/MWh^2
                  volume_unit: MWh^2
                  values: null
                d-LMPs: null
              aggregated_user_welfare:
                currecy: currecy
                welfare_vector:
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                - revenue: 0.8008281904610115
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
            users:
            - null
            - null
        FlexAsset:
          type: object
          properties:
            consumer_id:
              type: string
            reserve_market_offer_up:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh2'
            reserve_market_offer_down:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh2'
            location:
              $ref: '#/components/schemas/Location'
        CurtailableLoad:
          type: object
          properties:
            consumer_id:
              type: string
            unit:
              type: string
              enum:
              - KW
            power_vector:
              $ref: '#/components/schemas/PowerVector'
            location:
              $ref: '#/components/schemas/Location'
        FlexContract:
          type: object
          properties:
            name:
              type: string
            id:
              type: number
            gamma:
              type: number
          example:
            name: name
            id: 0.8008281904610115
            gamma: 6.027456183070403
        StorageUnit:
          required:
          - location
          type: object
          properties:
            power_capacity_KW:
              minimum: 0
              type: number
            energy_capacity_KWh:
              minimum: 0
              type: number
            inefficiency_rate_per_cent:
              maximum: 1
              minimum: 0
              type: number
            initial_SoC_per_cent:
              maximum: 1
              minimum: 0
              type: number
            final_SoC_per_cent:
              maximum: 1
              minimum: 0
              type: number
            location:
              $ref: '#/components/schemas/Location'
        Location:
          required:
          - id
          - name
          type: object
          properties:
            id:
              type: string
              enum:
              - DSO_AREA_1
              - DSO_AREA_2
              - DSO_AREA_3
              - DSO_AREA_4
              - DSO_AREA_5
            name:
              type: string
        DayOfferVector:
          maxItems: 25
          minItems: 23
          type: array
          items:
            $ref: '#/components/schemas/DayOfferVectorItem'
        DayOfferVectorItem:
          type: object
          properties:
            start_timestamp:
              type: string
              format: date-time
            end_timestamp:
              type: string
              format: date-time
            price:
              type: number
              format: currency
            volume:
              type: number
          example:
            volume: 6.027456183070403
            end_timestamp: 2000-01-23T04:56:07.000+00:00
            start_timestamp: 2000-01-23T04:56:07.000+00:00
            price: 0.8008281904610115
        RevenueVector:
          type: array
          items:
            $ref: '#/components/schemas/RevenueVectorItem'
        RevenueVectorItem:
          type: object
          properties:
            start_timestamp:
              type: string
              format: date-time
            end_timestamp:
              type: string
              format: date-time
            revenue:
              type: number
              format: currency
          example:
            revenue: 0.8008281904610115
            end_timestamp: 2000-01-23T04:56:07.000+00:00
            start_timestamp: 2000-01-23T04:56:07.000+00:00
        PowerVector:
          type: array
          items:
            $ref: '#/components/schemas/PowerVectorItem'
        PowerVectorItem:
          type: object
          properties:
            start_timestamp:
              type: string
              format: date-time
            end_timestamp:
              type: string
              format: date-time
            power:
              type: number
        DayOfferVectorEuroMWh:
          required:
          - price_unit
          - values
          - volume_unit
          type: object
          properties:
            values:
              $ref: '#/components/schemas/DayOfferVector'
            price_unit:
              type: string
              enum:
              - €/MWh
            volume_unit:
              type: string
              enum:
              - MWh
              - kWh
          example:
            price_unit: €/MWh
            volume_unit: MWh
            values:
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
            - volume: 6.027456183070403
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
              price: 0.8008281904610115
        Price_In_Euro:
          required:
          - currency
          - value
          type: object
          properties:
            value:
              type: number
            currency:
              type: string
              enum:
              - €
          example:
            currency: €
            value: 1.4658129805029452
        DayOfferVectorEuroMWh2:
          required:
          - price_unit
          - values
          - volume_unit
          type: object
          properties:
            values:
              $ref: '#/components/schemas/DayOfferVector'
            price_unit:
              type: string
              enum:
              - €/MWh^2
            volume_unit:
              type: string
              enum:
              - MWh^2
              - kWh^2
          example:
            price_unit: €/MWh^2
            volume_unit: MWh^2
            values: null
        DayOfferVectorEuroMVar:
          required:
          - price_unit
          - values
          - volume_unit
          type: object
          properties:
            values:
              $ref: '#/components/schemas/DayOfferVector'
            price_unit:
              type: string
              enum:
              - €/MVar
            volume_unit:
              type: string
              enum:
              - MVar
              - kVar
          example:
            price_unit: €/MVar
            volume_unit: MVar
            values: null
        FlexOffer:
          type: array
          items:
            $ref: '#/components/schemas/FlexOfferItem'
        FlexOfferItem:
          type: object
          properties:
            storage_unit:
              type: string
            day_ahead_market_offer:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh'
            reserve_market_offer_up:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh2'
            reserve_market_offer_down:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh2'
            d-LMPs:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh'
            q-LMPs:
              $ref: '#/components/schemas/DayOfferVectorEuroMVar'
            balancing_market_offer_up:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh'
            balancing_market_offer_down:
              $ref: '#/components/schemas/DayOfferVectorEuroMWh'
          example:
            balancing_market_offer_down: null
            q-LMPs:
              price_unit: €/MVar
              volume_unit: MVar
              values: null
            reserve_market_offer_down: null
            storage_unit: storage_unit
            balancing_market_offer_up: null
            day_ahead_market_offer:
              price_unit: €/MWh
              volume_unit: MWh
              values:
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
              - volume: 6.027456183070403
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
                price: 0.8008281904610115
            reserve_market_offer_up:
              price_unit: €/MWh^2
              volume_unit: MWh^2
              values: null
            d-LMPs: null
        StackedRevenuesResultRevenues:
          type: object
          properties:
            day_ahead_market_revenues:
              $ref: '#/components/schemas/Price_In_Euro'
            reserve_market_revenues:
              $ref: '#/components/schemas/Price_In_Euro'
            flexibility_market_revenues:
              $ref: '#/components/schemas/Price_In_Euro'
            balancing_market_revenues:
              $ref: '#/components/schemas/Price_In_Euro'
          example:
            balancing_market_revenues: null
            reserve_market_revenues: null
            flexibility_market_revenues: null
            day_ahead_market_revenues:
              currency: €
              value: 1.4658129805029452
        FlexOfferParams_time_granularity:
          type: object
          properties:
            id:
              type: string
            duration_seconds:
              type: integer
        FlexOfferResult_expected_revenues:
          type: object
          properties:
            currecy:
              type: string
            revenue_vector:
              $ref: '#/components/schemas/RevenueVector'
          example:
            currecy: currecy
            revenue_vector:
            - revenue: 0.8008281904610115
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
            - revenue: 0.8008281904610115
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
        PricingResult_aggregated_user_welfare:
          type: object
          properties:
            currecy:
              type: string
            welfare_vector:
              $ref: '#/components/schemas/RevenueVector'
          example:
            currecy: currecy
            welfare_vector:
            - revenue: 0.8008281904610115
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
            - revenue: 0.8008281904610115
              end_timestamp: 2000-01-23T04:56:07.000+00:00
              start_timestamp: 2000-01-23T04:56:07.000+00:00
        PricingResult_flex_contracts:
          type: object
          properties:
            flex_contract:
              $ref: '#/components/schemas/FlexContract'
            flexibility_revenues:
              $ref: '#/components/schemas/FlexOfferResult_expected_revenues'
            aggregated_user_welfare:
              $ref: '#/components/schemas/PricingResult_aggregated_user_welfare'
            flexibility:
              $ref: '#/components/schemas/FlexOffer'
          example:
            flex_contract:
              name: name
              id: 0.8008281904610115
              gamma: 6.027456183070403
            flexibility_revenues:
              currecy: currecy
              revenue_vector:
              - revenue: 0.8008281904610115
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
              - revenue: 0.8008281904610115
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
            flexibility:
            - balancing_market_offer_down: null
              q-LMPs:
                price_unit: €/MVar
                volume_unit: MVar
                values: null
              reserve_market_offer_down: null
              storage_unit: storage_unit
              balancing_market_offer_up: null
              day_ahead_market_offer:
                price_unit: €/MWh
                volume_unit: MWh
                values:
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
              reserve_market_offer_up:
                price_unit: €/MWh^2
                volume_unit: MWh^2
                values: null
              d-LMPs: null
            - balancing_market_offer_down: null
              q-LMPs:
                price_unit: €/MVar
                volume_unit: MVar
                values: null
              reserve_market_offer_down: null
              storage_unit: storage_unit
              balancing_market_offer_up: null
              day_ahead_market_offer:
                price_unit: €/MWh
                volume_unit: MWh
                values:
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
                - volume: 6.027456183070403
                  end_timestamp: 2000-01-23T04:56:07.000+00:00
                  start_timestamp: 2000-01-23T04:56:07.000+00:00
                  price: 0.8008281904610115
              reserve_market_offer_up:
                price_unit: €/MWh^2
                volume_unit: MWh^2
                values: null
              d-LMPs: null
            aggregated_user_welfare:
              currecy: currecy
              welfare_vector:
              - revenue: 0.8008281904610115
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
              - revenue: 0.8008281904610115
                end_timestamp: 2000-01-23T04:56:07.000+00:00
                start_timestamp: 2000-01-23T04:56:07.000+00:00
      requestBodies:
        StackedRevenuesParams:
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StackedRevenuesParams'
          required: true
        FlexOfferParams:
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlexOfferParams'
        PricingParams:
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PricingParams'
      securitySchemes:
        MyTokenAuth:
          type: oauth2
          flows:
            password:
              tokenUrl: https://db.flexgrid-project.eu/oauth/token
              scopes: {}
            clientCredentials:
              tokenUrl: https://db.flexgrid-project.eu/authorization
              scopes:
                post_stacked_revenues: post a stacked revenues scenario
          x-tokenInfoFunc: swagger_server.controllers.authorization_controller.check_MyTokenAuth
          x-scopeValidateFunc: swagger_server.controllers.authorization_controller.validate_scope_MyTokenAuth
    ```

3. Adapt the API to meet the goals of your endpoint

## 2. Connect to FLEXGRID Central Database

In order for your API endpoint to connect to use the FLEXGRID Central Database
authorization system, you need to perform the following:

1. Contact `prodromosmakris@mail.ntua.gr` to ask for client credentials for
   testing your API.

   You need to obtain:

   - `client_id`
   - `username`
   - `password`

2. Next step is to obtain a token. Post a curl request as follows:

   ```bash
   curl --location --request POST 'https://db.flexgrid-project.eu/oauth/token' \
   --form 'client_id="CLIENT_ID"' \
   --form 'grant_type="password"' \
   --form 'username="USERNAME"' \
   --form 'password="PASSWORD"'
   ```

   where `CLIENT_ID`, `USERNAME`, and `PASSWORD` are the credentials obtained in
   the previous step

   You should get a response like:

   ```json
   {
     "access_token": "THE_TOKEN",
     "expires_in": 3600,
     "token_type": "Bearer",
     "scope": "",
     "refresh_token": "THE_REFRESH_TOKEN"
   }
   ```

   where the value in `THE_TOKEN` is the token you need to test your API service

## 3. Test server locally

1. Visit https://editor.swagger.io/, and from the top menu select `Generate Server` --> `python-flask

   A file named `python-flask-server-generated.zip` should be downloaded by the
   browser

2. Unzip the file in a directory of your choice, and `cd` to it

3. Ensure that `python3` and `pip3` are installed

4. Due to [this
   bug](https://github.com/zalando/connexion/issues/739#issuecomment-514198578),
   you must enable make the following changes to file `./swagger_server/util.py`

   Replace

   ```python
   elif type(klass) == typing.GenericMeta:
     if klass.__extra__ == list:
         return _deserialize_list(data, klass.__args__[0])
     if klass.__extra__ == dict:
         return _deserialize_dict(data, klass.__args__[1])
   ```

   with

   ```python
   elif hasattr(klass, '__origin__'):
     if klass.__origin__ == list:
         return _deserialize_list(data, klass.__args__[0])
     if klass.__origin__ == dict:
         return _deserialize_dict(data, klass.__args__[1])
   ```

5. **Important** Replace the file
   `swagger_server/controllers/authorization_controller.py` with the
   corresponding one from this repository. The change is to add

   ```python
   import requests
   ```

   to the top, and

   ```python
    from typing import List
    import requests
    import os

    """
    controller generated to handled auth operation described at:
    https://connexion.readthedocs.io/en/latest/security.html
    """
    def check_MyTokenAuth(token):
        if not os.environ.get("SAMPLE_DATA"):
            auth = requests.get('https://db.flexgrid-project.eu/authorization/', params={
                'token': token,
                'resource': 'atp',
                'method': 'post',
            }).content
            if auth != b"OK":
                return None
        return {'scopes': ['read:pets', 'write:pets'], 'uid': 'test_value'}

    def validate_scope_MyTokenAuth(required_scopes, token_scopes):
        return set(required_scopes).issubset(set(token_scopes))



   ```

   in the beggining of `check_MyTokenAuth(token)` method

6. Add the logic for responding to each request, by editing the file controller
   files under `swagger_server/controllers/`. For example below we see a sample
   controller:

   ```python
   def scenarios_post(body):  # noqa: E501
       """Initiates a simulation scenario

       # noqa: E501

       :param body:
       :type body: list | bytes

       :rtype: ScenarioResult
       """
       if connexion.request.is_json:
           try:
               body = [ScenarioParamsInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

               result = [ScenarioResultInner.from_dict(
                   {
                       "date": str(p.sdate),
                       "countries": [],
                   }) for p in body]

               return result
           except Exception as e:
               logging.error(traceback.format_exc())
               return {'error_message': traceback.format_exc()}, 400

       return "Expecting JSON content type", 400
   ```

7. Configure the server to validate the types of the requests/responses.

   In file `swagger_server/__main__.py`, and replace the line

   ```python
   app.add_api('swagger.yaml', arguments={'title': 'Your title'}, pythonic_params=True)
   ```

   with

   ```python
   app.add_api('swagger.yaml',
               arguments={'title': 'Your title'},
               pythonic_params=True,
               strict_validation=True,
               validate_responses=True)
   ```

8. Install the required dependencies

   ```basd
   pip3 install -r requirements.txt
   ```

9. Run the server locally

   ```basd
   python3 -m swagger_server
   ```

10. You should be able to access protected resources using `curl`, with a
    request like

    ```bash
    curl --location --request POST 'http://localhost:8080/stacked_revenues' \
    --header 'Content-Type: application/vnd.api+json' \
    --header 'Authorization: Bearer THE_TOKEN' \
    --data-raw '{"sdate": "2020-10-16",
                "country": "GR",
                "markets": ["DAM", "BM"],
                "storage_units": [
                    {
                        "power_capacity_KW": 50,
                        "energy_capacity_KWh": 100,
                        "inefficiency_rate_per_cent": 0.999,
                        "initial_SoC_per_cent": 0.5,
                        "final_SoC_per_cent": 0.5,
                        "location": {
                            "id": "DSO_AREA_1",
                            "name": "string"
                        }
                    },
                                    {
                        "power_capacity_KW": 50,
                        "energy_capacity_KWh": 100,
                        "inefficiency_rate_per_cent": 0.999,
                        "initial_SoC_per_cent": 0.5,
                        "final_SoC_per_cent": 0.5,
                        "location": {
                            "id": "DSO_AREA_2",
                            "name": "string"
                        }
                    }
                ]}
    '
    ```

    where `THE_TOKEN` should be replaced with the one you got from step 2, and
    the URL and content of the message should be adapted to your endpoint.

## 4. Deploy on your server

This procedure is based on
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

It assumes os is Ubuntu 18.04, and outside facing web server is `nginx`.

We will use `uWSGi` as the application server for our application, which will
only be accessible through nginx.

1. Install required packages:

   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

   ```

2. Clone the projects repository, and the create a virtual environment for
   python

   ```bash
   git clone "REPOSITORY URL"
   cd project_dir/
   sudo apt install python3-venv
   python3 -m venv atpvenv
   source atpvenv/bin/activate
   ```

3. With the `venv` **activated**, run

   ```bash
   pip install wheel
   pip install uwsgi flask
   pip install -r requirements.txt
   ```

4. Add the files for usgi deployment

   File `app.py`

   ```python
   #!/usr/bin/env python3

   import connexion

   from swagger_server.encoder import JSONEncoder

   app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')

   app.app.json_encoder = JSONEncoder
   #   app.add_api('swagger.yaml', arguments={'title': 'Flexgrid ATP API'}, pythonic_params=True)
   app.add_api('swagger.yaml',
                     arguments={'title': 'Your title'},
                     pythonic_params=True,
                     strict_validation=True,
                     validate_responses=True)

   # set the WSGI application callable to allow using uWSGI:
   # uwsgi --http :8080 -w app
   application = app.app

   if __name__ == '__main__':
       # run our standalone gevent server
       app.run(port=8080)
   ```

   File `wsgi.py`

   ```python
   from app import application

   if __name__ == "__main__":
     appplication.run()
   ```

5. Test that the server can start with `wsgi`

   ```bash
   uwsgi --socket 127.0.0.1:5000 --protocol=http -w wsgi:application
   ```

   You can then test that it is responding on `localhost:5000`

6. Deactivate the venv

   ```bash
   deactivate
   ```

7. Create uwsgi configuration file as below:

   ```ini
   [uwsgi]
   module = wsgi:application

   master = true
   processes = 5

   socket = atp_service.sock
   chmod-socket = 660
   vacuum =true

   die-on-term = true
   ```

8. Add systemd configuration to automatically run the service:

    ```ini
    [Unit]
    Description=uWSGI instance to serve atp_service
    After=network.target eveoauth2.service nginx.service

    [Service]
    User=dss
    Group=www-data
    WorkingDirectory=/home/dss/flexgrid/atp_service
    Environment="PATH=/home/dss/flexgrid/atp_service/atpvenv/bin"
    ExecStart=/home/dss/flexgrid/atp_service/atpvenv/bin/uwsgi --ini atp_service.ini

    [Install]
    WantedBy=multi-user.target
    ```

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start atp.service
    sudo systemctl enable atp.service
    ```

9. Create nginx configuration as below, and the relevant certificates with certbot:

   ```nginx
   server {
       server_name atp.flexgrid-project.eu;

       location / {
         if ($request_method = 'OPTIONS') {
           add_header 'Access-Control-Allow-Origin' 'https://editor.swagger.io';
           add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
           #
           # Custom headers and headers various browsers *should* be OK with but aren't
           #
           add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization';
           #
           # Tell client that this pre-flight info is valid for 20 days
           #
           add_header 'Access-Control-Max-Age' 1728000;
           add_header 'Content-Type' 'text/plain; charset=utf-8';
           add_header 'Content-Length' 0;
           return 204;
         }
         if ($request_method = 'POST') {
           add_header 'Access-Control-Allow-Origin' 'https://editor.swagger.io';
           add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
           add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization';
           add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
         }
         if ($request_method = 'GET') {
           add_header 'Access-Control-Allow-Origin' 'https://editor.swagger.io';
           add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
           add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization';
           add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
         }

         include uwsgi_params;
         uwsgi_pass unix:/home/dss/flexgrid/atp_service/atp_service.sock;
       }



       listen 443 ssl; # managed by Certbot
       ssl_certificate /etc/letsencrypt/live/atp.flexgrid-project.eu/fullchain.pem; # managed by Certbot
       ssl_certificate_key /etc/letsencrypt/live/atp.flexgrid-project.eu/privkey.pem; # managed by Certbot
       include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
       ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

   }

   server {
       if ($host = atp.flexgrid-project.eu) {
           return 301 https://$host$request_uri;
       } # managed by Certbot


       listen 80;
       server_name atp.flexgrid-project.eu;
       return 404; # managed by Certbot
   }
   ```

9. Validate that the service is working:

   ```bash
   curl --location --request POST 'https://atp.flexgrid-project.eu/scenarios' \
   --header 'Content-Type: application/json' \
   --header 'Authorization: Bearer THE_TOKEN' \
   --data-raw '[

   ]'
   ```

## Implementation of the algorithm

The algorithm that has been imported in this example is found in this
repo:
https://github.com/FlexGrid/stacked_revenues

In order to integrate the algorithm you can add your repo as a git
submodule. The command for adding a submodule is:

```bash
git submodule add https://github.com/namespace/repository
```

Then you can call the submodule code from the controller that was
generated by codegen.

The following code is the example for calling the example submodule:

Controller:

```python
import connexion
import six

from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server import util
from swagger_server.adapters.stacked_revenues_adapter import stacked_revenues_adapter

import logging
import traceback


def stacked_revenues_post(body):  # noqa: E501
    """Initiates a simulation scenario for Stacked Revenues maximization

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StackedRevenuesResult
    """
    if connexion.request.is_json:
        try:
            body = StackedRevenuesParams.from_dict(connexion.request.get_json())  # noqa: E501
    
            result = stacked_revenues_adapter(body)

            return result
        except Exception as e:
            logging.error(traceback.format_exc())
            return {'error_message': traceback.format_exc()}, 400

    return "Expecting JSON content type", 400
```

The `stacked_revenues_adapter` function is defined in its own file:

```python
from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server.models.day_offer_vector_euro_m_wh import DayOfferVectorEuroMWh  # noqa: E501
from swagger_server.models.day_offer_vector_euro_m_wh2 import DayOfferVectorEuroMWh2  # noqa: E501
from swagger_server.models.day_offer_vector_euro_m_var import DayOfferVectorEuroMVar  # noqa: E501
from swagger_server.models.price_in_euro import PriceInEuro  # noqa: E501
from stacked_revenues.maximize_stacked_revenues import battery_portfolio
from swagger_server.adapters.market_adapter import MarketAdapter
from datetime import datetime, timedelta
import dateutil.parser


def stacked_revenues_adapter(stacked_revenues_params):
    assert isinstance(stacked_revenues_params, StackedRevenuesParams)

    ns = len(stacked_revenues_params.storage_units)
    print(f"We got {ns} batteries")

    martketAdapter = MarketAdapter(
        datetime.combine(stacked_revenues_params.sdate, datetime.min.time()),
        datetime.combine(stacked_revenues_params.sdate, datetime.min.time()) +
        timedelta(days=1) - timedelta(minutes=1))

    timestamps = [(
        (dateutil.parser.isoparse(martketAdapter.start_timestamp) +
         timedelta(hours=t)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        (dateutil.parser.isoparse(martketAdapter.start_timestamp) +
         timedelta(hours=t+1)).strftime('%Y-%m-%dT%H:%M:%SZ'),
    ) for t in range(24)]

    print(f"min time {datetime.min.time()} timestamps= {timestamps}")

    dam_participation = "DAM" in stacked_revenues_params.markets
    rm_participation = "RM" in stacked_revenues_params.markets
    fm_participation = "FM" in stacked_revenues_params.markets
    bm_participation = "BM" in stacked_revenues_params.markets

    dam_prices = [obj['value'] for obj in martketAdapter.day_ahead_market()]
    print(f"dam_prices= {len(dam_prices)}")
    rup_prices = [obj['value']
                  for obj in martketAdapter.reserve_market()]
    rdn_prices = [obj['value']
                  for obj in martketAdapter.reserve_market()]

    fmp_prices = martketAdapter.fmp(
        [su.location.id for su in stacked_revenues_params.storage_units])
    fmq_prices = martketAdapter.fmq(
        [su.location.id for su in stacked_revenues_params.storage_units])
    bm_up_prices = [obj['value']
                    for obj in martketAdapter.balancing_market_up()]
    print(f"bm_up_prices= {len(bm_up_prices)}")

    bm_dn_prices = [obj['value']
                    for obj in martketAdapter.balancing_market_down()]
    print(f"bm_dn_prices= {len(bm_dn_prices)}")

    p_max = [obj.power_capacity_kw for obj in stacked_revenues_params.storage_units]
    print(f"p_max= {p_max}")

    E_max = [obj.energy_capacity_k_wh for obj in stacked_revenues_params.storage_units]
    print(f"E_max= {E_max}")

    roundtrip_eff = [
        obj.inefficiency_rate_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"roundtrip_eff= {roundtrip_eff}")

    E0 = [obj.initial_so_c_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"E0= {E0}")

    ET = [obj.final_so_c_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"ET= {ET}")

    # Create a battery object
    bsu = battery_portfolio(ns, dam_participation, rm_participation, fm_participation, bm_participation, dam_prices,
                            rup_prices, rdn_prices, fmp_prices, fmq_prices, bm_up_prices, bm_dn_prices,
                            p_max, E_max, roundtrip_eff, E0, ET)

    # Maximize stacked revenues
    [Profits, pup, pdn, dam_schedule, rup_commitment, rdn_commitment, pflexibility, qflexibility,
        soc, DAM_profits, RM_profits, FM_profits, BM_profits] = bsu.maximize_stacked_revenues()

    print(f"\nProfits= {Profits},\n\n"
          f"pup = {pup},\n\n"
          f"pdn = {pdn},\n\n"
          f"dam_schedule = {dam_schedule},\n\n"
          f"rup_commitment = {rup_commitment},\n\n"
          f"rdn_commitment = {rdn_commitment},\n\n"
          f"pflexibility = {pflexibility},\n\n"
          f"qflexibility = {qflexibility},\n\n"
          f"soc = {soc},\n\n"
          f"DAM_profits = {DAM_profits},\n\n"
          f"RM_profits = {RM_profits},\n\n"
          f"FM_profits = {FM_profits},\n\n"
          f"BM_profits = {BM_profits}\n")

    return StackedRevenuesResult.from_dict({
        "sdate": str(stacked_revenues_params.sdate),
        "flex_offer": [{
            "location": stacked_revenues_params.storage_units[su_ind].location.id,
            "day_ahead_market_offer": build_market_offer_mwh(timestamps, dam_schedule[su_ind]).to_dict(),
            "reserve_market_offer_up": build_market_offer_mwh2(timestamps, rup_commitment[su_ind]).to_dict(),
            "reserve_market_offer_down": build_market_offer_mwh2(timestamps, rdn_commitment[su_ind]).to_dict(),
            "d-LMPs":  build_market_offer_mwh(timestamps, pflexibility[su_ind]),
            "q-LMPs": build_market_offer_mvar(timestamps, qflexibility[su_ind]),
            "balancing_market_offer_up": build_market_offer_mwh(timestamps, pup[su_ind]).to_dict(),
            "balancing_market_offer_down": build_market_offer_mwh(timestamps, pdn[su_ind]).to_dict()
        } for su_ind in range(len(stacked_revenues_params.storage_units))],
        "revenues": {
            "day_ahead_market_revenues": build_profits(DAM_profits).to_dict(),
            "reserve_market_revenues": build_profits(RM_profits).to_dict(),
            "flexibility_market_revenues": build_profits(FM_profits).to_dict(),
            "balancing_market_revenues": build_profits(BM_profits).to_dict(),
        }
    })


def build_market_offer_mwh(timestamps, schedule):
    return DayOfferVectorEuroMWh.from_dict({
        "values": [{
            "start_timestamp": timestamps[i][0],
            "end_timestamp": timestamps[i][1],
            "volume": round(schedule[i],2),
        } for i in range(len(timestamps))],
        "price_unit": "€/MWh",
        "volume_unit": "kWh"
    })


def build_market_offer_mwh2(timestamps, schedule):
    return DayOfferVectorEuroMWh2.from_dict({
        "values": [{
            "start_timestamp": timestamps[i][0],
            "end_timestamp": timestamps[i][1],
            "volume": round(schedule[i],2),
        } for i in range(len(timestamps))],
        "price_unit": f"€/MWh^2",
        "volume_unit": "kWh^2"
    })


def build_market_offer_mvar(timestamps, schedule):
    return DayOfferVectorEuroMVar.from_dict({
        "values": [{
            "start_timestamp": timestamps[i][0],
            "end_timestamp": timestamps[i][1],
            "volume": round(schedule[i],2),
        } for i in range(len(timestamps))],
        "price_unit": "€/MVar",
        "volume_unit": "kVar"
    })


def build_profits(price):
    return PriceInEuro.from_dict({'value': price, 'currency': '€'})

```

## Using external data

In order to use data from an external API, you can create an adapter
file. Here is exapmle code for retrieving the data from Fingrid and
Nordpool markers:

market_adapter:

```python
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
from . nordpool_auth_client import NordpoolAuthClient
import dateutil.parser


class MarketAdapter:
    def __init__(self, start_timestamp, end_timestamp):
        load_dotenv()

        self.start_timestamp = datetime.utcfromtimestamp(
            start_timestamp.timestamp()).replace(minute=0, second=0).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.end_timestamp = datetime.utcfromtimestamp(
            end_timestamp.timestamp()).replace(minute=0, second=0).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.market_ids = {
            79: 'Frequency containment reserve for normal operation, hourly market prices',
            244: 'Up-regulating price in the balancing power market',
            106: 'Down-regulation price in the balancing market',
        }

    def fingrid(self, market_id):

        url = f"https://api.fingrid.fi/v1/variable/{market_id}/events/json"
        headers = {'x-api-key': os.environ.get("FINGRID_TOKEN")}
        return json.loads(requests.request("GET", url, params={
            'start_time': self.start_timestamp,
            'end_time': self.end_timestamp},
            headers=headers).content)

    def nordpool(self, deliveryarea):
        url = f"https://marketdata-api.nordpoolgroup.com/dayahead/prices/area"
        headers = NordpoolAuthClient().auth_headers()
        # print(f"The headers are {headers}")
        params = {
            'deliveryarea': deliveryarea,
            'status': 'O',
            'currency': 'EUR',
            'startTime': self.start_timestamp,
            'endTime':  (dateutil.parser.isoparse(self.end_timestamp) + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        }
        print(f"The params are --> {params}")
        result = requests.request("GET", url, params=params,
                                  headers=headers)

        # print(f"The result is --> {json.loads(result.content)[0]['values']}")
        return [{'value': val['value'], 'start_time': val['startTime'], 'end_time': val['endTime']} for val in json.loads(result.content)[0]['values']]

    def fmp(self, location_ids):
        dataset = {'DSO_AREA_1': [0] * 24,
                   'DSO_AREA_2': [-100.27, -100.27, -10.27, -10.27, -10.27, -10.27, 0, 0, -9.59, -9.59,
                                  -9.54, -15, -15, -15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'DSO_AREA_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15,
                                  3.55, 3.01, 3.01, 3.44, 3.41, 13.74, 12.02, 15, 12.55, 12.53, 12.04, 8.55, 2.98],
                   'DSO_AREA_4': [-10.27, -10.27, -10.27, -10.27, -10.27, -10.27, -10.27, -10.01, -9.92, -9.54, -9.17,
                                  -15, -15, -15, -9.26, -9.54, -9.54, -9.17, 1.83, 1.55, -9.65, 1.02, 0.61, 0.61],
                   'DSO_AREA_5': [2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 3.36, 3.25, 15, 15, 3.54, 3.54, 3.54, 15,
                                  15, 15, 15, 15, 12.57, 12, 12.07, 15, 15], }

        return [dataset[lid] for lid in location_ids]

    def fmq(self, location_ids):
        dataset = {'DSO_AREA_1': [0] * 24,
                   'DSO_AREA_2': [-6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -0.05, -0.25, -6.88, -6.88, -6.87, -10.61,
                                  -10.4, -10.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'DSO_AREA_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11.24, 3, 3, 3, 3, 3, 10.34, 9.12,
                                  10.54, 8.83, 8.82, 8.69, 6.41, 3],
                   'DSO_AREA_4': [-6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -6.94, -6.93, -6.87, -6.82, -10.62,
                                  -10.62, -10.62, -6.83, -6.87, -6.87, -6.82, 0.93, 0.79, -6.89, 0.52, 0.31, 0.31],
                   'DSO_AREA_5': [3, 3, 3, 3, 3, 3, 3, 3, 3, 11.24, 10.85, 3, 3, 3, 10.94, 11.24, 11.24, 10.85, 10.54,
                                  8.83, 9.11, 8.67, 11, 11], }

        return [dataset[lid] for lid in location_ids]

    def day_ahead_market(self):
        if os.environ.get("SAMPLE_DATA"):
            result = json.loads("""[
                {
                    "category": "dayAhead",
                    "createdTime": 1601462571635,
                    "type": "price",
                    "SubType": "area",
                    "resolution": "PT1H",
                    "unit": "EUR/MWh",
                    "scale": 2,
                    "startTime": "2020-10-15T21:00:00Z",
                    "endTime": "2020-10-16T21:00:00Z",
                    "values": [
                        {
                            "startTime": "2020-10-15T21:00:00Z",
                            "endTime": "2020-10-15T22:00:00Z",
                            "value": 20.01
                        },
                        {
                            "startTime": "2020-10-15T22:00:00Z",
                            "endTime": "2020-10-15T23:00:00Z",
                            "value": 20.13
                        },
                        {
                            "startTime": "2020-10-15T23:00:00Z",
                            "endTime": "2020-10-16T00:00:00Z",
                            "value": 19.7
                        },
                        {
                            "startTime": "2020-10-16T00:00:00Z",
                            "endTime": "2020-10-16T01:00:00Z",
                            "value": 19.56
                        },
                        {
                            "startTime": "2020-10-16T01:00:00Z",
                            "endTime": "2020-10-16T02:00:00Z",
                            "value": 19.57
                        },
                        {
                            "startTime": "2020-10-16T02:00:00Z",
                            "endTime": "2020-10-16T03:00:00Z",
                            "value": 19.96
                        },
                        {
                            "startTime": "2020-10-16T03:00:00Z",
                            "endTime": "2020-10-16T04:00:00Z",
                            "value": 35.23
                        },
                        {
                            "startTime": "2020-10-16T04:00:00Z",
                            "endTime": "2020-10-16T05:00:00Z",
                            "value": 50.03
                        },
                        {
                            "startTime": "2020-10-16T05:00:00Z",
                            "endTime": "2020-10-16T06:00:00Z",
                            "value": 54.29
                        },
                        {
                            "startTime": "2020-10-16T06:00:00Z",
                            "endTime": "2020-10-16T07:00:00Z",
                            "value": 66.22
                        },
                        {
                            "startTime": "2020-10-16T07:00:00Z",
                            "endTime": "2020-10-16T08:00:00Z",
                            "value": 62.34
                        },
                        {
                            "startTime": "2020-10-16T08:00:00Z",
                            "endTime": "2020-10-16T09:00:00Z",
                            "value": 56.59
                        },
                        {
                            "startTime": "2020-10-16T09:00:00Z",
                            "endTime": "2020-10-16T10:00:00Z",
                            "value": 52.9
                        },
                        {
                            "startTime": "2020-10-16T10:00:00Z",
                            "endTime": "2020-10-16T11:00:00Z",
                            "value": 52.84
                        },
                        {
                            "startTime": "2020-10-16T11:00:00Z",
                            "endTime": "2020-10-16T12:00:00Z",
                            "value": 52.79
                        },
                        {
                            "startTime": "2020-10-16T12:00:00Z",
                            "endTime": "2020-10-16T13:00:00Z",
                            "value": 45.23
                        },
                        {
                            "startTime": "2020-10-16T13:00:00Z",
                            "endTime": "2020-10-16T14:00:00Z",
                            "value": 44.57
                        },
                        {
                            "startTime": "2020-10-16T14:00:00Z",
                            "endTime": "2020-10-16T15:00:00Z",
                            "value": 46.42
                        },
                        {
                            "startTime": "2020-10-16T15:00:00Z",
                            "endTime": "2020-10-16T16:00:00Z",
                            "value": 58.44
                        },
                        {
                            "startTime": "2020-10-16T16:00:00Z",
                            "endTime": "2020-10-16T17:00:00Z",
                            "value": 59.68
                        },
                        {
                            "startTime": "2020-10-16T17:00:00Z",
                            "endTime": "2020-10-16T18:00:00Z",
                            "value": 58.56
                        },
                        {
                            "startTime": "2020-10-16T18:00:00Z",
                            "endTime": "2020-10-16T19:00:00Z",
                            "value": 39.59
                        },
                        {
                            "startTime": "2020-10-16T19:00:00Z",
                            "endTime": "2020-10-16T20:00:00Z",
                            "value": 35.96
                        },
                        {
                            "startTime": "2020-10-16T20:00:00Z",
                            "endTime": "2020-10-16T21:00:00Z",
                            "value": 26.48
                        }
                    ],
                    "attributes": [
                        {
                            "role": null,
                            "name": "deliveryArea",
                            "value": "FI"
                        },
                        {
                            "role": null,
                            "name": "status",
                            "value": "O"
                        },
                        {
                            "role": null,
                            "name": "currency",
                            "value": "EUR"
                        },
                        {
                            "role": null,
                            "name": "confirmationStatus",
                            "value": "confirmed"
                        }
                    ]
                }
            ] """)
            return [{'value': val['value'], 'start_time': val['startTime'], 'end_time': val['endTime']} for val in result[0]['values']]
        return self.nordpool('FI')

    def balancing_market_up(self):
        if os.environ.get("SAMPLE_DATA"):
            return json.loads("""[
                {
                    "value": 20.010000,
                    "start_time": "2020-10-15T21:00:00+0000",
                    "end_time": "2020-10-15T22:00:00+0000"
                },
                {
                    "value": 20.130000,
                    "start_time": "2020-10-15T22:00:00+0000",
                    "end_time": "2020-10-15T23:00:00+0000"
                },
                {
                    "value": 19.700000,
                    "start_time": "2020-10-15T23:00:00+0000",
                    "end_time": "2020-10-16T00:00:00+0000"
                },
                {
                    "value": 19.560000,
                    "start_time": "2020-10-16T00:00:00+0000",
                    "end_time": "2020-10-16T01:00:00+0000"
                },
                {
                    "value": 19.570000,
                    "start_time": "2020-10-16T01:00:00+0000",
                    "end_time": "2020-10-16T02:00:00+0000"
                },
                {
                    "value": 19.960000,
                    "start_time": "2020-10-16T02:00:00+0000",
                    "end_time": "2020-10-16T03:00:00+0000"
                },
                {
                    "value": 35.230000,
                    "start_time": "2020-10-16T03:00:00+0000",
                    "end_time": "2020-10-16T04:00:00+0000"
                },
                {
                    "value": 50.030000,
                    "start_time": "2020-10-16T04:00:00+0000",
                    "end_time": "2020-10-16T05:00:00+0000"
                },
                {
                    "value": 54.290000,
                    "start_time": "2020-10-16T05:00:00+0000",
                    "end_time": "2020-10-16T06:00:00+0000"
                },
                {
                    "value": 66.220000,
                    "start_time": "2020-10-16T06:00:00+0000",
                    "end_time": "2020-10-16T07:00:00+0000"
                },
                {
                    "value": 62.340000,
                    "start_time": "2020-10-16T07:00:00+0000",
                    "end_time": "2020-10-16T08:00:00+0000"
                },
                {
                    "value": 100.590000,
                    "start_time": "2020-10-16T08:00:00+0000",
                    "end_time": "2020-10-16T09:00:00+0000"
                },
                {
                    "value": 52.900000,
                    "start_time": "2020-10-16T09:00:00+0000",
                    "end_time": "2020-10-16T10:00:00+0000"
                },
                {
                    "value": 52.840000,
                    "start_time": "2020-10-16T10:00:00+0000",
                    "end_time": "2020-10-16T11:00:00+0000"
                },
                {
                    "value": 52.790000,
                    "start_time": "2020-10-16T11:00:00+0000",
                    "end_time": "2020-10-16T12:00:00+0000"
                },
                {
                    "value": 45.230000,
                    "start_time": "2020-10-16T12:00:00+0000",
                    "end_time": "2020-10-16T13:00:00+0000"
                },
                {
                    "value": 44.570000,
                    "start_time": "2020-10-16T13:00:00+0000",
                    "end_time": "2020-10-16T14:00:00+0000"
                },
                {
                    "value": 46.420000,
                    "start_time": "2020-10-16T14:00:00+0000",
                    "end_time": "2020-10-16T15:00:00+0000"
                },
                {
                    "value": 58.440000,
                    "start_time": "2020-10-16T15:00:00+0000",
                    "end_time": "2020-10-16T16:00:00+0000"
                },
                {
                    "value": 80.000000,
                    "start_time": "2020-10-16T16:00:00+0000",
                    "end_time": "2020-10-16T17:00:00+0000"
                },
                {
                    "value": 58.560000,
                    "start_time": "2020-10-16T17:00:00+0000",
                    "end_time": "2020-10-16T18:00:00+0000"
                },
                {
                    "value": 39.590000,
                    "start_time": "2020-10-16T18:00:00+0000",
                    "end_time": "2020-10-16T19:00:00+0000"
                },
                {
                    "value": 35.960000,
                    "start_time": "2020-10-16T19:00:00+0000",
                    "end_time": "2020-10-16T20:00:00+0000"
                },
                {
                    "value": 52.500000,
                    "start_time": "2020-10-16T20:00:00+0000",
                    "end_time": "2020-10-16T21:00:00+0000"
                }
            ]""")
        return self.fingrid(244)

    def balancing_market_down(self):
        if os.environ.get("SAMPLE_DATA"):
            return json.loads("""[
                {
                    "value": 20.010000,
                    "start_time": "2020-10-15T21:00:00+0000",
                    "end_time": "2020-10-15T22:00:00+0000"
                },
                {
                    "value": 20.130000,
                    "start_time": "2020-10-15T22:00:00+0000",
                    "end_time": "2020-10-15T23:00:00+0000"
                },
                {
                    "value": 19.700000,
                    "start_time": "2020-10-15T23:00:00+0000",
                    "end_time": "2020-10-16T00:00:00+0000"
                },
                {
                    "value": 19.560000,
                    "start_time": "2020-10-16T00:00:00+0000",
                    "end_time": "2020-10-16T01:00:00+0000"
                },
                {
                    "value": 19.570000,
                    "start_time": "2020-10-16T01:00:00+0000",
                    "end_time": "2020-10-16T02:00:00+0000"
                },
                {
                    "value": 19.960000,
                    "start_time": "2020-10-16T02:00:00+0000",
                    "end_time": "2020-10-16T03:00:00+0000"
                },
                {
                    "value": 35.230000,
                    "start_time": "2020-10-16T03:00:00+0000",
                    "end_time": "2020-10-16T04:00:00+0000"
                },
                {
                    "value": 24.500000,
                    "start_time": "2020-10-16T04:00:00+0000",
                    "end_time": "2020-10-16T05:00:00+0000"
                },
                {
                    "value": 54.290000,
                    "start_time": "2020-10-16T05:00:00+0000",
                    "end_time": "2020-10-16T06:00:00+0000"
                },
                {
                    "value": 28.000000,
                    "start_time": "2020-10-16T06:00:00+0000",
                    "end_time": "2020-10-16T07:00:00+0000"
                },
                {
                    "value": 28.000000,
                    "start_time": "2020-10-16T07:00:00+0000",
                    "end_time": "2020-10-16T08:00:00+0000"
                },
                {
                    "value": 56.590000,
                    "start_time": "2020-10-16T08:00:00+0000",
                    "end_time": "2020-10-16T09:00:00+0000"
                },
                {
                    "value": 52.900000,
                    "start_time": "2020-10-16T09:00:00+0000",
                    "end_time": "2020-10-16T10:00:00+0000"
                },
                {
                    "value": 52.840000,
                    "start_time": "2020-10-16T10:00:00+0000",
                    "end_time": "2020-10-16T11:00:00+0000"
                },
                {
                    "value": 52.790000,
                    "start_time": "2020-10-16T11:00:00+0000",
                    "end_time": "2020-10-16T12:00:00+0000"
                },
                {
                    "value": 24.500000,
                    "start_time": "2020-10-16T12:00:00+0000",
                    "end_time": "2020-10-16T13:00:00+0000"
                },
                {
                    "value": 24.500000,
                    "start_time": "2020-10-16T13:00:00+0000",
                    "end_time": "2020-10-16T14:00:00+0000"
                },
                {
                    "value": 18.500000,
                    "start_time": "2020-10-16T14:00:00+0000",
                    "end_time": "2020-10-16T15:00:00+0000"
                },
                {
                    "value": 26.000000,
                    "start_time": "2020-10-16T15:00:00+0000",
                    "end_time": "2020-10-16T16:00:00+0000"
                },
                {
                    "value": 59.680000,
                    "start_time": "2020-10-16T16:00:00+0000",
                    "end_time": "2020-10-16T17:00:00+0000"
                },
                {
                    "value": 58.560000,
                    "start_time": "2020-10-16T17:00:00+0000",
                    "end_time": "2020-10-16T18:00:00+0000"
                },
                {
                    "value": 39.590000,
                    "start_time": "2020-10-16T18:00:00+0000",
                    "end_time": "2020-10-16T19:00:00+0000"
                },
                {
                    "value": 16.000000,
                    "start_time": "2020-10-16T19:00:00+0000",
                    "end_time": "2020-10-16T20:00:00+0000"
                },
                {
                    "value": 26.480000,
                    "start_time": "2020-10-16T20:00:00+0000",
                    "end_time": "2020-10-16T21:00:00+0000"
                }
            ]""")


        return self.fingrid(106)

    def reserve_market(self):
        if os.environ.get("SAMPLE_DATA"):
            return json.loads("""[
                {
                    "value": 5.240000,
                    "start_time": "2020-10-15T21:00:00+0000",
                    "end_time": "2020-10-15T22:00:00+0000"
                },
                {
                    "value": 9.850000,
                    "start_time": "2020-10-15T22:00:00+0000",
                    "end_time": "2020-10-15T23:00:00+0000"
                },
                {
                    "value": 9.940000,
                    "start_time": "2020-10-15T23:00:00+0000",
                    "end_time": "2020-10-16T00:00:00+0000"
                },
                {
                    "value": 9.850000,
                    "start_time": "2020-10-16T00:00:00+0000",
                    "end_time": "2020-10-16T01:00:00+0000"
                },
                {
                    "value": 9.850000,
                    "start_time": "2020-10-16T01:00:00+0000",
                    "end_time": "2020-10-16T02:00:00+0000"
                },
                {
                    "value": 9.150000,
                    "start_time": "2020-10-16T02:00:00+0000",
                    "end_time": "2020-10-16T03:00:00+0000"
                },
                {
                    "value": 9.310000,
                    "start_time": "2020-10-16T03:00:00+0000",
                    "end_time": "2020-10-16T04:00:00+0000"
                },
                {
                    "value": 12.770000,
                    "start_time": "2020-10-16T04:00:00+0000",
                    "end_time": "2020-10-16T05:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T05:00:00+0000",
                    "end_time": "2020-10-16T06:00:00+0000"
                },
                {
                    "value": 12.120000,
                    "start_time": "2020-10-16T06:00:00+0000",
                    "end_time": "2020-10-16T07:00:00+0000"
                },
                {
                    "value": 12.500000,
                    "start_time": "2020-10-16T07:00:00+0000",
                    "end_time": "2020-10-16T08:00:00+0000"
                },
                {
                    "value": 12.000000,
                    "start_time": "2020-10-16T08:00:00+0000",
                    "end_time": "2020-10-16T09:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T09:00:00+0000",
                    "end_time": "2020-10-16T10:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T10:00:00+0000",
                    "end_time": "2020-10-16T11:00:00+0000"
                },
                {
                    "value": 12.690000,
                    "start_time": "2020-10-16T11:00:00+0000",
                    "end_time": "2020-10-16T12:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T12:00:00+0000",
                    "end_time": "2020-10-16T13:00:00+0000"
                },
                {
                    "value": 12.120000,
                    "start_time": "2020-10-16T13:00:00+0000",
                    "end_time": "2020-10-16T14:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T14:00:00+0000",
                    "end_time": "2020-10-16T15:00:00+0000"
                },
                {
                    "value": 12.880000,
                    "start_time": "2020-10-16T15:00:00+0000",
                    "end_time": "2020-10-16T16:00:00+0000"
                },
                {
                    "value": 13.080000,
                    "start_time": "2020-10-16T16:00:00+0000",
                    "end_time": "2020-10-16T17:00:00+0000"
                },
                {
                    "value": 14.000000,
                    "start_time": "2020-10-16T17:00:00+0000",
                    "end_time": "2020-10-16T18:00:00+0000"
                },
                {
                    "value": 9.000000,
                    "start_time": "2020-10-16T18:00:00+0000",
                    "end_time": "2020-10-16T19:00:00+0000"
                },
                {
                    "value": 8.850000,
                    "start_time": "2020-10-16T19:00:00+0000",
                    "end_time": "2020-10-16T20:00:00+0000"
                },
                {
                    "value": 7.920000,
                    "start_time": "2020-10-16T20:00:00+0000",
                    "end_time": "2020-10-16T21:00:00+0000"
                }
            ]""")

        return self.fingrid(79)
```

The client for authenticating to nordpool service is the following:

```python
import base64
import json
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


class NordpoolAuthClient:

    token = {}
    # url = f"https://sts.nordpoolgroup.com/connect/token"

    def __init__(self):
        load_dotenv()

    def get_token(self):
        headers = {
            'Authorization': f"Basic {base64.b64encode('client_marketdata_api:client_marketdata_api'.encode('utf-8')).decode('utf-8')}",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # print(f"headers: {headers} user {os.environ.get('NORDPOOL_USERNAME')} pass {os.environ.get('NORDPOOL_PASSWORD')}")
        __class__.token = json.loads(
            requests.post(
                'https://sts.nordpoolgroup.com/connect/token',
                data={
                    'grant_type': 'password',
                    'scope': 'marketdata_api',
                    'username': os.environ.get("NORDPOOL_USERNAME"),
                    'password': os.environ.get("NORDPOOL_PASSWORD"),
                },
                headers=headers
            ).content)
        __class__.token['acquired_at'] = datetime.utcnow()

    def have_valid_token(self):
        return __class__.token and 'acquired_at' in __class__.token and 'expires_in' in __class__.token and (__class__.token['acquired_at'] + timedelta(seconds=__class__.token['expires_in'] - 30) > datetime.utcnow())

    def auth_headers(self):

        if not self.have_valid_token():
            self.get_token()

        return {'Ocp-Apim-Subscription-Key':  os.environ.get("NORDPOOL_SUBSCRIPTION_KEY"),
                'Authorization': f"Bearer {__class__.token['access_token']}"}
```

## Tests with sample data

To test with local data (without relying on any external services),
you can set the `SAMPLE_DATA=1` environment variable.

Run your server like this:

```bash
SAMPLE_DATA=1 python3 -m swagger_server
```

Then you can send a curl request like the follwoing:

```curl
curl --location --request POST 'http://localhost:8080/stacked_revenues' \
--header 'Content-Type: application/vnd.api+json' \
--header 'Authorization: Bearer q9R95vDAHOMumaANPTNKjCd5aeSSk2' \
--data-raw '{"sdate": "2020-10-16",
            "country": "GR",
            "markets": ["DAM", "BM"],
            "storage_units": [
                {a
                    "power_capacity_KW": 50,
                    "energy_capacity_KWh": 100,
                    "inefficiency_rate_per_cent": 0.999,
                    "initial_SoC_per_cent": 0.5,
                    "final_SoC_per_cent": 0.5,
                    "location": {
                        "id": "DSO_AREA_1",
                        "name": "string"
                    }
                },
                                {
                    "power_capacity_KW": 50,
                    "energy_capacity_KWh": 100,
                    "inefficiency_rate_per_cent": 0.999,
                    "initial_SoC_per_cent": 0.5,
                    "final_SoC_per_cent": 0.5,
                    "location": {
                        "id": "DSO_AREA_2",
                        "name": "string"
                    }
                }
            ]}
'
```

And you should get a result like this:

```json
{
    "flex_offer": [
        {
            "balancing_market_offer_down": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 50.25
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 50.2
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 50.05
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.17
                    }
                ],
                "volume_unit": "kWh"
            },
            "balancing_market_offer_up": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 49.75
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 49.8
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 99.83
                    }
                ],
                "volume_unit": "kWh"
            },
            "d-LMPs": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": -0.5
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": -0.4
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": -50.05
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 99.65
                    }
                ],
                "volume_unit": "kWh"
            },
            "day_ahead_market_offer": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": -0.03
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": -0.05
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.25
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.2
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": -49.83
                    }
                ],
                "volume_unit": "kWh"
            },
            "location": "DSO_AREA_1",
            "q-LMPs": {
                "price_unit": "€/MVar",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.0
                    }
                ],
                "volume_unit": "kVar"
            },
            "reserve_market_offer_down": {
                "price_unit": "€/MWh^2",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.0
                    }
                ],
                "volume_unit": "kWh^2"
            },
            "reserve_market_offer_up": {
                "price_unit": "€/MWh^2",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.0
                    }
                ],
                "volume_unit": "kWh^2"
            }
        },
        {
            "balancing_market_offer_down": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 50.25
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 50.2
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 50.05
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.17
                    }
                ],
                "volume_unit": "kWh"
            },
            "balancing_market_offer_up": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 49.75
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 49.8
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 99.83
                    }
                ],
                "volume_unit": "kWh"
            },
            "d-LMPs": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": -0.5
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": -0.4
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": -50.05
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 49.9
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": -100.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 99.65
                    }
                ],
                "volume_unit": "kWh"
            },
            "day_ahead_market_offer": {
                "price_unit": "€/MWh",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": -0.03
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": -0.05
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.25
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.2
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": -50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 50.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": -49.83
                    }
                ],
                "volume_unit": "kWh"
            },
            "location": "DSO_AREA_2",
            "q-LMPs": {
                "price_unit": "€/MVar",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.0
                    }
                ],
                "volume_unit": "kVar"
            },
            "reserve_market_offer_down": {
                "price_unit": "€/MWh^2",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.0
                    }
                ],
                "volume_unit": "kWh^2"
            },
            "reserve_market_offer_up": {
                "price_unit": "€/MWh^2",
                "values": [
                    {
                        "end_timestamp": "2020-10-15T22:00:00Z",
                        "start_timestamp": "2020-10-15T21:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-15T23:00:00Z",
                        "start_timestamp": "2020-10-15T22:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T00:00:00Z",
                        "start_timestamp": "2020-10-15T23:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T01:00:00Z",
                        "start_timestamp": "2020-10-16T00:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T02:00:00Z",
                        "start_timestamp": "2020-10-16T01:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T03:00:00Z",
                        "start_timestamp": "2020-10-16T02:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T04:00:00Z",
                        "start_timestamp": "2020-10-16T03:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T05:00:00Z",
                        "start_timestamp": "2020-10-16T04:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T06:00:00Z",
                        "start_timestamp": "2020-10-16T05:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T07:00:00Z",
                        "start_timestamp": "2020-10-16T06:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T08:00:00Z",
                        "start_timestamp": "2020-10-16T07:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T09:00:00Z",
                        "start_timestamp": "2020-10-16T08:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T10:00:00Z",
                        "start_timestamp": "2020-10-16T09:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T11:00:00Z",
                        "start_timestamp": "2020-10-16T10:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T12:00:00Z",
                        "start_timestamp": "2020-10-16T11:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T13:00:00Z",
                        "start_timestamp": "2020-10-16T12:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T14:00:00Z",
                        "start_timestamp": "2020-10-16T13:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T15:00:00Z",
                        "start_timestamp": "2020-10-16T14:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T16:00:00Z",
                        "start_timestamp": "2020-10-16T15:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T17:00:00Z",
                        "start_timestamp": "2020-10-16T16:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T18:00:00Z",
                        "start_timestamp": "2020-10-16T17:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T19:00:00Z",
                        "start_timestamp": "2020-10-16T18:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T20:00:00Z",
                        "start_timestamp": "2020-10-16T19:00:00Z",
                        "volume": 0.0
                    },
                    {
                        "end_timestamp": "2020-10-16T21:00:00Z",
                        "start_timestamp": "2020-10-16T20:00:00Z",
                        "volume": 0.0
                    }
                ],
                "volume_unit": "kWh^2"
            }
        }
    ],
    "revenues": {
        "balancing_market_revenues": {
            "currency": "€",
            "value": 49.59638526603818
        },
        "day_ahead_market_revenues": {
            "currency": "€",
            "value": 7.686546558905
        },
        "flexibility_market_revenues": {
            "currency": "€",
            "value": -6.7827000126063925
        },
        "reserve_market_revenues": {
            "currency": "€",
            "value": 0.0
        }
    },
    "sdate": "2020-10-16"
}
```


## Original Instructions Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080//ui/
```

Your Swagger definition lives here:

```
http://localhost:8080//swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
